from django.db import models

from Protocols.base import Base 
from Protocols.models import Protocol

class SIP(Base, models.Model):
    protocol          = models.ForeignKey(Protocol)
    extension         = models.CharField(max_length=15)
    secret            = models.CharField(max_length=15)
    voice_mail_status = models.BooleanField()

