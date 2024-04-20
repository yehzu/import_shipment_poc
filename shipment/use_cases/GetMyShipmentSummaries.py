from shipment.ports.gateways.ContainerGateway import ContainerGateway
from shipment.ports.gateways.InvoiceGateway import InvoiceGateway
from shipment.ports.gateways.ShipmentGateway import ShipmentGateway
from shipment.ports.in_bound.IMyShipmentSummaries import IMyShipmentSummaries
from shipment.ports.out_bound.IShipmentSummariesResult import IMyShipmentsResult
from shipment.ports.out_bound.ShipmentSummary import ShipmentSummary


def _aggregate_shipment_summaries_from(shipment, balances, containers) -> ShipmentSummary:
    ss = ShipmentSummary()

    ss.mbl_number = shipment.mbl_number
    ss.container_numbers = [c.container_number for c in containers]
    ss.container_sizes = [c.size for c in containers]

    ap = [b for b in balances if b.invoice_type == "ap"][0]
    ss.ap_last_paid_date = ap.last_paid_date
    ss.ap_balance_currency = ap.currency
    ss.ap_balance_amount = ap.amount

    ar = [b for b in balances if b.invoice_type == "ar"][0]
    ss.ar_last_paid_date = ar.last_paid_date
    ss.ar_balance_currency = ar.currency
    ss.ar_balance_amount = ar.amount

    return ss


class GetMyShipmentSummaries(IMyShipmentSummaries):
    def __init__(self, shipment_gw: ShipmentGateway, invoice_gw: InvoiceGateway, container_gw: ContainerGateway,
                 presenter: IMyShipmentsResult):
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
