from import_shipment.biz.gateways.MblGateway import MblGateway
from import_shipment.biz.gateways.TradePartnerGateway import TradePartnerGateway
from import_shipment.biz.inbound.IImportShipment import IImportShipment
from import_shipment.biz.gateways.PayloadInterpreter import PayloadInterpreter
from import_shipment.biz.outbound.ImportMblResult import ImportMblResult
from import_shipment.impl.use_cases.TradePartnerMapper import TradePartnerMapper


class ImportShipment(IImportShipment):

    def __init__(self, payload_interpreter: PayloadInterpreter, mbl_gateway: MblGateway,
                 tp_gateway: TradePartnerGateway, presenter: ImportMblResult):
        self.payload_interpreter = payload_interpreter
        self.mbl_gateway = mbl_gateway
        self.trade_partner_gateway = tp_gateway
        self.presenter = presenter

    def import_mbl(self, tenant: str, import_mbl_payload: str):

        try:
            mbl = self.payload_interpreter.interpret_payload(import_mbl_payload)
        except:
            self.presenter.present_error("fail to parse input payload")
            return

        # business logic put here
        if self.mbl_gateway.exist(mbl.mbl_number):
            self.presenter.present_skip("MBL already exists")
            return

        tp_mapper = TradePartnerMapper(self.trade_partner_gateway, tenant)
        mbl.trade_partner = tp_mapper.map(mbl.trade_partner)

        try:
            self.mbl_gateway.create_shipment(mbl)
        except:
            self.presenter.present_error("fail to create MBL")
            return

        self.presenter.present("success")
