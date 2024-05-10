from django.db import models


# Create your models here.

# use a Dj prefix to distinguish the entities and Django models
class DjUploadRecord(models.Model):
    upload_status = models.CharField(max_length=100)
    upload_payload = models.CharField(max_length=100)
    mapped_mbl = models.CharField(max_length=100)
