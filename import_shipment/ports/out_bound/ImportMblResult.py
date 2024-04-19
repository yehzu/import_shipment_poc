from import_shipment.ports.out_bound import ObImportMblResponse


class ImportMblResult:
    def present(self, resp: ObImportMblResponse):
        pass

    def present_skip(self, msg):
        pass

    def present_error(self, msg):
        pass
