from import_shipment.entities.Mbl import Mbl


class MblGateway:
    def exist(self, mbl_number: str) -> bool:
        pass

    def create_shipment(self, mbl: Mbl):
        pass

    def find_most_similar(self, tenant: str, trade_partner: str):
        pass
