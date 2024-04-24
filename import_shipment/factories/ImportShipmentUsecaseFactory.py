from import_shipment.factories.MblGatewayFactory import MblGatewayFactory
from import_shipment.factories.PayloadInterpreterFactory import PayloadInterpreterFactory
from import_shipment.factories.TradePartnerGatewayFactory import TradePartnerGatewayFactory
from import_shipment.ports.in_bound.IImportShipment import IImportShipment
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult
from import_shipment.presenters.JsonPresenter import JsonPresenter
from import_shipment.use_cases.ImportShipment import ImportShipment
from import_shipment.use_cases.ImportShipmentCustForSuperPro import ImportShipmentCustForSuperPro


class ImportShipmentUsecaseFactory:

    @staticmethod
    def get(tenant, vendor, payload_format, version) -> (IImportShipment, ImportMblResult):

        interpreter = PayloadInterpreterFactory.get(f'{vendor}-{payload_format}-{version}')
        presenter = JsonPresenter()

        match (tenant, vendor):
            case (_, "super-pro"):
                # for customization
                other_gw = OtherGatewayImpl()
                return ImportShipmentCustForSuperPro(interpreter, other_gw, presenter), presenter
            case (_, _):
                # default use case
                mbl_repo = MblGatewayFactory.get()
                tp_repo = TradePartnerGatewayFactory.get()
                return ImportShipment(interpreter, mbl_repo, tp_repo, presenter), presenter
