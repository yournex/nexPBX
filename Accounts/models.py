from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Account(models.Model):
    ACC_STATUS_CHOICES = (
        (u'enable', 'enable'),
        (u'deleted', 'deleted'),
    )

    CLIENT_TYPE_CHOICES = (
        (u'user', 'User'),
        (u'gateway', 'Gateway'),
    )

    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=10, choices= CLIENT_TYPE_CHOICES)
    user_status = models.CharField(max_length=10, choices= ACC_STATUS_CHOICES)

    pass


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
