from shipment.entities.InvoiceBalance import InvoiceBalance
from shipment.entities.Shipment import Shipment


class InvoiceGateway:
    def get_balances_per_shipment(self, tenant, shipments) -> dict[Shipment, tuple[InvoiceBalance, InvoiceBalance]]:
        # return shipment to (AR balance, AP balance)
        pass
