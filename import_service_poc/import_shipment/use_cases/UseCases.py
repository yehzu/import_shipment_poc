from import_shipment. ports.gateways.MblGateway import MblGateway
from import_shipment. ports.gateways.TradePartnerGateway import TradePartnerGateway
from import_shipment. ports.in_bound.ImportMbl import ImportMbl
from import_shipment. ports.in_bound.PayloadInterpreter import PayloadInterpreter
from import_shipment. ports.out_bound.ObImportMblResponse import ObImportMblResponse
from import_shipment. ports.out_bound.ImportMblResult import ImportMblResult
from import_shipment. use_cases.TradePartnerMapper import TradePartnerMapper


class UseCases(ImportMbl):

    def import_mbl(self, tenant: str, import_mbl_payload: str, payload_interpreter: PayloadInterpreter,
                   mbl_gateway: MblGateway, trade_partner_gateway: TradePartnerGateway, presenter: ImportMblResult):

        mbl = payload_interpreter.interpret_payload(import_mbl_payload)

        status = "success"
        # business logic put here
        if mbl_gateway.exist(mbl.mbl_number):
            status = "existed"
        else:
            tp_mapper = TradePartnerMapper(trade_partner_gateway, tenant)
            mbl.trade_partner = tp_mapper.map(mbl.trade_partner)

            try:
                mbl_gateway.create_shipment(mbl)
            except:
                print("Error creating")
                status = "fail"

        ob_resp = ObImportMblResponse()
        ob_resp.mbl_number = mbl.mbl_number
        ob_resp.status = status
        # produce side effect to the world
        presenter.present(ob_resp)
