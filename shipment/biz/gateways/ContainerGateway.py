from shipment.biz.entities import Container
from shipment.biz.entities import Shipment


class ContainerGateway:

    def get_containers_per_shipment(self, tenant, shipments) -> dict[Shipment, list[Container]]:
        pass

    def get_or_create_containers(self, tenant, office, containers: list[Container]) -> list[str]:
        pass
