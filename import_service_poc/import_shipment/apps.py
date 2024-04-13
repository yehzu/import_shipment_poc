from django.apps import AppConfig


class ImportShipmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'import_shipment'

    def ready(self) -> None:
        from import_shipment.views import import_fast_pro_ftp_schedule
        import_fast_pro_ftp_schedule()
