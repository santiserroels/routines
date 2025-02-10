from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField, CharField, TimeField
from django.contrib.postgres.fields import ArrayField

DAYS = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)


class Routine(Model):
    user = ForeignKey("app.User", on_delete=CASCADE, related_name="routines")
    days = ArrayField(CharField(max_length=255, choices=DAYS, blank=True, default=1))
    hour = TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    title = CharField(max_length=255, blank=True, null=True)
    exercises = ManyToManyField("app.Exercise")


class Exercise(Model):
    title = CharField(max_length=255, blank=True, null=True)
