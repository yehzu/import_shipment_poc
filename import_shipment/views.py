from import_shipment.factories.ImportShipmentUsecaseFactory import ImportShipmentUsecaseFactory
from import_shipment.presenters.JsonPresenter import JsonPresenter


# Create your views here.


# handler for route /shipment/fast-pro/xml/v1
def import_shipment(request, vendor, payload_format, version):
    tenant = "test tenant"  # or other way to get tenant, maybe in the header?
    mbl_payload = request.body  # or other way to get the payload (e.g. http body, or AS2 protocol)

    usecase, presenter = ImportShipmentUsecaseFactory.get(tenant, vendor, payload_format, version)
    usecase.import_mbl(tenant, mbl_payload)

    return presenter.get_view_model()
