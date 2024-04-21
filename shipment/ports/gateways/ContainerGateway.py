from shipment.entities.Container import Container
from shipment.entities.InvoiceBalance import InvoiceBalance
from shipment.entities.Shipment import Shipment


class ContainerGateway:

    def get_containers_per_shipment(self, tenant, shipments) -> dict[Shipment, list[Container]]:
        pass
