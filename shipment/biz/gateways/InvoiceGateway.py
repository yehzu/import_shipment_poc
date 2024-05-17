from shipment.biz.entities import InvoiceBalance, Invoice
from shipment.biz.entities import Shipment


class InvoiceGateway:
    def get_balances_per_shipment(self, tenant, shipments) -> dict[Shipment, tuple[InvoiceBalance, InvoiceBalance]]:
        # return shipment to (AR balance, AP balance)
        pass

    def get_or_create_invoices(self, tenant, office, invoices: list[Invoice]) -> list[str]:
        pass
