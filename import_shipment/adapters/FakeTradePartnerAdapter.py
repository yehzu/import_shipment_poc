from import_shipment.ports.gateways.TradePartnerGateway import TradePartnerGateway


class FakeTradePartnerAdapter(TradePartnerGateway):
    def find_most_similar(self, tenant, trade_partner):
        return "hahahaha: " + trade_partner  # just a fake
