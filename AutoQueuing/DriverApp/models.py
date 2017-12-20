from __future__ import unicode_literals

from django.db import models


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



