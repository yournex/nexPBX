from django.db import models

from Protocols.base import Base

class SIP(Base, models.Model):
    extension         = models.CharField(max_length=15)
    secret            = models.CharField(max_length=15)
    voice_mail_status = models.BooleanField()

