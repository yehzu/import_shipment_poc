from shipment.entities.InvoiceBalance import InvoiceBalance
from shipment.entities.Shipment import Shipment


class InvoiceGateway:
    def get_balances_per_shipment(self, tenant, shipments) -> dict[Shipment, list[InvoiceBalance]]:

        pass
