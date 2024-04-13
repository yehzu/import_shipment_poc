from import_shipment.entities.Mbl import Mbl
from import_shipment.ports.gateways.MblGateway import MblGateway
from import_shipment.ports.gateways.TradePartnerGateway import TradePartnerGateway


class GoFreightAdapter(MblGateway, TradePartnerGateway):
    gofreight_client = ""  # client lib for accessing external api

    def create_shipment(self, mbl: Mbl):
        super().create_shipment(mbl)

    def exist(self, mbl_number: str) -> bool:
        return self.gofreight_client.get_mbl(mbl_number) is not None

    def find_most_similar(self, tenant, trade_partner):
        tp_list = self.gofreight_client.get_trade_partners(tenant)
        # logic for lookup most similar tp by trade_partner from tp_list
        # here just assign self to the most similar
        most_similar_tp = trade_partner
        return most_similar_tp
