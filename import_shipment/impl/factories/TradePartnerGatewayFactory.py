from import_shipment.impl.adapters import FakeTradePartnerAdapter
from import_shipment.impl.adapters.GoFreightAdapter import GoFreightAdapter
from import_shipment.biz.gateways import TradePartnerGateway


class TradePartnerGatewayFactory:
    @staticmethod
    def get(repo_type="fake-local-dev") -> TradePartnerGateway:
        if repo_type == "gofreight-external-api":
            return GoFreightAdapter()
        elif repo_type == "fake-local-dev":
            return FakeTradePartnerAdapter()
        else:
            raise NotImplementedError
