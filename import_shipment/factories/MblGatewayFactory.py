from import_shipment.adapters.FakeMblAdapter import FakeMblAdapter
from import_shipment.adapters.GoFreightAdapter import GoFreightAdapter
from import_shipment.ports.gateways.MblGateway import MblGateway


class MblGatewayFactory:
    @staticmethod
    def get(repo_type="fake-local-dev") -> MblGateway:
        if repo_type == "gofreight-external-api":
            return GoFreightAdapter()
        elif repo_type == "fake-local-dev":
            return FakeMblAdapter()
        else:
            raise NotImplementedError
