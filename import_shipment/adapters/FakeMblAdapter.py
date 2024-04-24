from import_shipment.ports.gateways.MblGateway import MblGateway


class FakeMblAdapter(MblGateway):
    def exist(self, mbl_number: str) -> bool:
        return False
