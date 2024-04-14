from import_shipment.factories.MblGatewayFactory import MblGatewayFactory
from import_shipment.factories.PayloadInterpreterFactory import PayloadInterpreterFactory
from import_shipment.factories.TradePartnerGatewayFactory import TradePartnerGatewayFactory
from import_shipment.presenters.JsonPresenter import JsonPresenter
from import_shipment.factories.ImportShipmentUseCaseFactory import ImportShipmentUseCaseFactory


# Create your views here.


# handler for route /shipment/fast-pro/xml/v1
def import_fast_pro_xml_v1(request):
    tenant = "test tenant"  # or other way to get tenant, maybe in the header?
    mbl_payload = request.body  # or other way to get the payload (e.g. http body, or AS2 protocol)

    interpreter = PayloadInterpreterFactory.get("fast-pro-xml-v1")
    mbl_repo = MblGatewayFactory.get()
    tp_repo = TradePartnerGatewayFactory.get()

    presenter = JsonPresenter()

    usecase = ImportShipmentUseCaseFactory.get(tenant, "office")
    usecase.import_mbl(tenant, mbl_payload, interpreter, mbl_repo, tp_repo, presenter)

    return presenter.get_view_model()
