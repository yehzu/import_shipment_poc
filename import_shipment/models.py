from django.db import models


# Create your models here.
class AuditLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    mbl_number = models.CharField(max_length=200)
    action = models.CharField(max_length=10)
