from django.test import TestCase
from shipment.adapters.FakeAdapter import FakeAdapter
from shipment.presenters.FakePresenter import FakePresenter
from shipment.use_cases.GetMyShipmentSummaries import GetMyShipmentSummaries


# Create your tests here.

class GetShipmentSummariesTest(TestCase):

    def test_get_shipment_summaries(self):
        shipment_gw = FakeAdapter()
        invoice_gw = shipment_gw
        container_gw = shipment_gw
        presenter = FakePresenter()
        use_case = GetMyShipmentSummaries(shipment_gw, invoice_gw, container_gw, presenter)

        use_case.get_my_shipment_summaries("tenant", "office", "my_role", "")
