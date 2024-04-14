from import_shipment.ports.gateways.MblGateway import MblGateway
from import_shipment.ports.gateways.TradePartnerGateway import TradePartnerGateway
from import_shipment.ports.in_bound.ImportMbl import ImportMbl
from import_shipment.ports.in_bound.PayloadInterpreter import PayloadInterpreter
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult


class CustomizedUseCasesB(ImportMbl):

    def import_mbl(self, tenant: str, import_mbl_payload: str, payload_interpreter: PayloadInterpreter,
                   mbl_gateway: MblGateway, trade_partner_gateway: TradePartnerGateway, presenter: ImportMblResult):
        # another implementation for something?
        pass
