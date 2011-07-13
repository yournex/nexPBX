from django.db import models

from Services.base import Base


class SIP(Base):
    extension         = models.CharField(max_length=15)
    secret            = models.CharField(max_length=15)
    voice_mail_status = models.BooleanField()

