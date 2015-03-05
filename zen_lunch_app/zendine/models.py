from django.db import models
from django.utils import timezone

class User(models.Model):
    TIME_1200 = '12pm'
    TIME_1230 = '12:30pm'
    TIME_1300 = '1:00pm'
    ZEN_LUNCH_TIME_CHOICES = (
        (TIME_1200, "12:00 PM"),
        (TIME_1230, "12:30 PM"),
        (TIME_1300, "1:00 PM"),
    )
    email = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    team = models.CharField(max_length=100, null=True)
    enabled = models.BooleanField(default=True)
    create_date = models.DateTimeField(verbose_name="user creation time", default=timezone.now, null=True)
    zen_lunch_time = models.CharField(max_length=7, choices = ZEN_LUNCH_TIME_CHOICES)

class Lunch(models.Model):
    lunch_date = models.DateTimeField()
    create_date = models.DateTimeField(default=timezone.now, null=True)

class UserLunch(models.Model):
    lunch = models.ForeignKey(Lunch)
    user = models.ForeignKey(User)
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("lunch", "user")

class UserBlacklist(models.Model):
    user = models.ForeignKey(User, related_name="blacklist_user_id")
    blocked_user = models.ForeignKey(User, related_name="blocked_user_id")
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("user", "blocked_user")