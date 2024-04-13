import json

from django.http import JsonResponse

from import_shipment.ports.Presenter import Presenter
from import_shipment.ports.out_bound import ObImportMblResponse
from import_shipment.ports.out_bound.ImportMblResult import ImportMblResult


class JsonPresenter(ImportMblResult, Presenter):
    def __init__(self):
        self.view_model = None

    def present(self, resp: ObImportMblResponse):
        self.view_model = resp.__dict__
        print(json.dumps(self.view_model))

    def get_view_model(self):
        return JsonResponse(self.view_model)
