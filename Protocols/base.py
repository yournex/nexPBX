from django.db import models

class Base:
    CLIENT_TYPE_CHOICES = (
        (u'user', 'User'),
        (u'gateway', 'Gateway'),
    )

    PRO_TYPE_CHOICES = (
        (u'voip', 'Voip'),
        (u'chat', 'Chat'),
    )
    name        = models.CharField(max_length=60)
    client_type = models.CharField(max_length=1, choices= CLIENT_TYPE_CHOICES)
