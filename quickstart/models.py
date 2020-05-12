from django.db import models
import datetime

# Create your models here.


class member(models.Model):
    real_name = models.CharField(max_length=120)
    tz = models.CharField(max_length=120)

    def __str__(self):
        return "%s %s" % (self.real_name, self.tz)


class activity_period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    member = models.ForeignKey(
        member, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.start_time, self.end_time)

    class Meta:
        ordering = ['start_time']
