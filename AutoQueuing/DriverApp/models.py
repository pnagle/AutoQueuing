from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.timesince import timesince
from django.utils import timezone


class Driver(models.Model):
    """
    Driver table to store driver details, demo purpose using only id
    """

    driver_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return str(self.driver_id)


class Customer(models.Model):
    """
    Customer table to store user details, demo purpose using only id
    """

    customer_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return str(self.customer_id)


class Request(models.Model):
    """
    Requests table to store request details
    """

    status_choices = (
        (0, 'waiting'),
        (1, 'ongoing'),
        (2, 'complete')
    )

    request_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer')
    driver_id = models.ForeignKey('Driver', null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    picked_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=status_choices, default=0)
    request_location_lat = models.DecimalField(max_digits=15, decimal_places=11)
    request_location_long = models.DecimalField(max_digits=15, decimal_places=11)

    def get_time_diff(self):
        # requested_at = datetime.datetime(Request.objects.filter(request_id=self.request_id).values('requested_at'))
        dt1 = datetime.combine(self.requested_at,self.t1)
        dt2 = datetime.combine(datetime.datetime.now(), self.t2)
        return timesince(dt1, dt2)   # Assuming dt2 is the more recent time

    def humanizeTimeDiff(self, timestamp = None):
        """
        Returns a humanized string representing time difference
        between now() and the input timestamp.

        The output rounds up to days, hours, minutes, or seconds.
        4 days 5 hours returns '4 days'
        0 days 4 hours 3 minutes returns '4 hours', etc...
        """
        if timestamp is None:
            timestamp = self.requested_at
        # print timestamp
        # print datetime.datetime.now()

        timeDiff = timezone.now() - timestamp
        days = timeDiff.days
        hours = timeDiff.seconds/3600
        minutes = timeDiff.seconds%3600/60
        seconds = timeDiff.seconds%3600%60

        str = ""
        tStr = ""
        if days > 0:
            if days == 1:   tStr = "day"
            else:           tStr = "days"
            str = str + "%s %s" %(days, tStr)
            return str
        elif hours > 0:
            if hours == 1:  tStr = "hour"
            else:           tStr = "hours"
            str = str + "%s %s" %(hours, tStr)
            return str
        elif minutes > 0:
            if minutes == 1:tStr = "min"
            else:           tStr = "mins"
            str = str + "%s %s" %(minutes, tStr)
            return str
        elif seconds > 0:
            if seconds == 1:tStr = "sec"
            else:           tStr = "secs"
            str = str + "%s %s" %(seconds, tStr)
            return str
        else:
            return None

    def humanizePickedTimeDiff(self):
        return self.humanizeTimeDiff(self.picked_at)

    def humanizeCompletedTimeDiff(self):
        return self.humanizeTimeDiff(self.completed_at)


