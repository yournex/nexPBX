from django.db import models

class Protocols(models.Model):
    PRO_TYPE_CHOICES = (
        (u'voip', 'Voip'),
        (u'chat', 'Chat'),
    )

    pro_type  = models.CharField(max_length=1, choices= PRO_TYPE_CHOICES)
    name      = models.CharField(max_length=30)
    disabled  = models.BooleanField()
    installed = models.BooleanField()
    package   = models.CharField(max_length=60) 

