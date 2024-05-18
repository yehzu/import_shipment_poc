from shipment.biz.gateways.ContainerGateway import ContainerGateway
from shipment.biz.gateways.InvoiceGateway import InvoiceGateway
from shipment.biz.gateways.ShipmentGateway import ShipmentGateway
from shipment.biz.inbound.IMyShipmentSummaries import IMyShipmentSummaries
from shipment.biz.outbound.IShipmentSummariesResult import IShipmentSummariesResult
from shipment.biz.outbound.ShipmentSummary import ShipmentSummary, ContainerSummary, BalanceSummary


def _transform_balance_summary_from(balance) -> BalanceSummary:
    ib = BalanceSummary()

    ib.currency = balance.currency
    ib.balance_amount = balance.amount
    ib.last_paid_date = balance.last_paid_date

    return ib


def _transform_container_summary_from(container) -> ContainerSummary:
    cs = ContainerSummary()

    cs.container_number = container.container_number
    cs.size = container.size

    return cs


def _aggregate_shipment_summaries_from(shipment, balances, containers) -> ShipmentSummary:
    #
    ss = ShipmentSummary()

    ss.mbl_number = shipment.mbl_number

    ss.containers = [_transform_container_summary_from(c) for c in containers]

    (ar, ap) = balances
    ss.ar = _transform_balance_summary_from(ar)
    ss.ap = _transform_balance_summary_from(ap)

    return ss


class GetMyShipmentSummaries(IMyShipmentSummaries):
    def __init__(self, shipment_gw: ShipmentGateway, invoice_gw: InvoiceGateway, container_gw: ContainerGateway,
                 presenter: IShipmentSummariesResult):
        self.shipment_gw = shipment_gw
        self.invoice_gw = invoice_gw
        self.container_gw = container_gw
        self.presenter = presenter

    def get_my_shipment_summaries(self, tenant, office, my_role, shipment_filters):

        try:
            shipments = self.shipment_gw.get_shipments(tenant, office, my_role)
            balances_per_shipment = self.invoice_gw.get_balances_per_shipment(tenant, shipments)
            containers_per_shipment = self.container_gw.get_containers_per_shipment(tenant, shipments)
        except:
            self.presenter.present_failure("fail to gather information, reason: xxx")
            return

        result = \
            [_aggregate_shipment_summaries_from(
                s,
                balances_per_shipment[s],
                containers_per_shipment[s])
                for s in shipments]

        self.presenter.present(result)
