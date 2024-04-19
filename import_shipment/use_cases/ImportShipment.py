from import_shipment.ports.gateways.MblGateway import MblGateway
from import_shipment.ports.gateways.TradePartnerGateway import TradePartnerGateway
from import_shipment.ports.in_bound.IImportShipment import IImportShipment
from import_shipment.ports.gateways.PayloadInterpreter import PayloadInterpreter
from import_shipment.ports.out_bound.ObImportMblResponse import ObImportMblResponse
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult
from import_shipment.use_cases.TradePartnerMapper import TradePartnerMapper


class InputInvalidException:
    pass


class InternalServiceException:
    pass


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
            print("Error interpreting payload")
            raise InputInvalidException

        status = "success"
        # business logic put here
        if self.mbl_gateway.exist(mbl.mbl_number):
            status = "existed"
        else:
            tp_mapper = TradePartnerMapper(self.trade_partner_gateway, tenant)
            mbl.trade_partner = tp_mapper.map(mbl.trade_partner)

            try:
                self.mbl_gateway.create_shipment(mbl)
            except:
                print("Error creating")
                raise InternalServiceException

        ob_resp = ObImportMblResponse()
        ob_resp.mbl_number = mbl.mbl_number
        ob_resp.status = status
        # produce side effect to the world
        self.presenter.present(ob_resp)
