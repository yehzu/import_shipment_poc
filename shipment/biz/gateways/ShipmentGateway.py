from shipment.biz.entities import Shipment


class ShipmentGateway:
    def get_shipments(self, tenant, office, my_role) -> list[Shipment]:
        pass

    def create_shipment(self, tenant, office, my_role, shipment: Shipment) -> str:
        pass
