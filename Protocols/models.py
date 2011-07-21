from django.db import models


from Accounts.models import Account

class Protocol(models.Model):
    STATUS_CHOICES = (
        (u'0', 'Disable'),
        (u'1', 'Enable'),
    )

    account = models.ForeignKey(Account)
    name    = models.CharField(max_length=30)
    status  = models.CharField(max_length=1, choices=STATUS_CHOICES)

