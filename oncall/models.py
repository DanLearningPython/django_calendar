from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True)

class EventType(models.Model):
    event_type_name = models.CharField(max_length=50, blank=False, unique=True)
    event_type_abbrev = models.CharField(max_length=50, blank=False)
    event_type_color= models.CharField(max_length=50, blank=True)
    event_type_order = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "%s" % (self.event_type_name)


class Event(models.Model):
    event_name = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=False)
    event_start = models.DateTimeField(default=datetime.now)
    event_end = models.DateTimeField(default=datetime.now)
    event_notes = models.CharField(max_length=255, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()