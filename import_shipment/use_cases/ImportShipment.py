from import_shipment.entities.UploadRecord import UploadRecord
from import_shipment.ports.gateways.MblGateway import MblGateway
from import_shipment.ports.gateways.TradePartnerGateway import TradePartnerGateway
from import_shipment.ports.gateways.UploadRecordGateway import UploadRecordGateway
from import_shipment.ports.in_bound.IImportShipment import IImportShipment
from import_shipment.ports.gateways.PayloadInterpreter import PayloadInterpreter
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult
from import_shipment.use_cases.TradePartnerMapper import TradePartnerMapper


class ImportShipment(IImportShipment):

    def __init__(self, payload_interpreter: PayloadInterpreter, mbl_gateway: MblGateway,
                 tp_gateway: TradePartnerGateway,
                 upload_record_gw: UploadRecordGateway,
                 presenter: ImportMblResult):
        self.payload_interpreter = payload_interpreter
        self.mbl_gateway = mbl_gateway
        self.trade_partner_gateway = tp_gateway
        self.upload_record_gw = upload_record_gw
        self.presenter = presenter

    def import_mbl(self, tenant: str, import_mbl_payload: str):
        """
        this use case is to import a MBL to shipment gateway from a string payload
        at the same time, record the import status for the user to review
        """

        ur = UploadRecord()
        ur.upload_payload = import_mbl_payload

        try:
            mbl = self.payload_interpreter.interpret_payload(import_mbl_payload)
        except:
            ur.upload_status = "failed to parse input payload"
            self.upload_record_gw.save_record(ur)
            self.presenter.present_error("fail to parse input payload")
            return

        # business logic put here
        if self.mbl_gateway.exist(mbl.mbl_number):
            ur.upload_status = "skip: MBL already exists"
            self.upload_record_gw.save_record(ur)
            self.presenter.present_skip("MBL already exists")
            return

        tp_mapper = TradePartnerMapper(self.trade_partner_gateway, tenant)
        mbl.trade_partner = tp_mapper.map(mbl.trade_partner)

        ur.mbl = mbl
        try:
            self.mbl_gateway.create_shipment(mbl)
        except:
            ur.upload_status = "gateway error: failed to create"
            self.upload_record_gw.save_record(ur)
            self.presenter.present_error("fail to create MBL")
            return

        ur.upload_status = "success"
        self.upload_record_gw.save_record(ur)
        self.presenter.present("success")
