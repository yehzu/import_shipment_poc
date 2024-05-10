import json

from import_shipment.entities.UploadRecord import UploadRecord
from import_shipment.models import DjUploadRecord
from import_shipment.ports.gateways.UploadRecordGateway import UploadRecordGateway


class SqlLiteAdapter(UploadRecordGateway):
    def save_record(self, ur: UploadRecord):
        # Django's Model should go here
        DjUploadRecord.objects.create(
            upload_status=ur.upload_status,
            upload_payload=ur.upload_payload,
            mapped_mbl=json.dumps(ur.mapped_mbl.__dict__)
        )
