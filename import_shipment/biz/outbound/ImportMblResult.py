from import_shipment.biz.outbound import ObImportMblResponse


class ImportMblResult:
    def present(self, resp: ObImportMblResponse):
        pass

    def present_skip(self, msg):
        pass

    def present_error(self, msg):
        pass
