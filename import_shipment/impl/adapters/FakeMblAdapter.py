from import_shipment.biz.gateways.MblGateway import MblGateway


class FakeMblAdapter(MblGateway):
    def exist(self, mbl_number: str) -> bool:
        return True
