from import_shipment.entities.Mbl import Mbl
from import_shipment.models import AuditLog
from import_shipment.ports.gateways.MblGateway import MblGateway


class AuditMblAdapter(MblGateway):

    def __init__(self, mbl_gw: MblGateway):
        self.adapter = mbl_gw

    def exist(self, mbl_number: str) -> bool:
        AuditLog.objects.create(
            mbl_number=mbl_number,
            action="exist"
        )
        return self.adapter.exist(mbl_number)

    def create_shipment(self, mbl: Mbl):
        AuditLog.objects.create(
            mbl_number=mbl.mbl_number,
            action="create"
        )
        return self.adapter.create_shipment(mbl)
