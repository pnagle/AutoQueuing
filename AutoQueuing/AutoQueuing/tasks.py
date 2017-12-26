from AutoQueuing.celeryapp import app as celery
from DriverApp.models import Request
from django.utils import timezone
from celery.contrib import rdb


@celery.task
def update_ongoing_request(pk):
    rdb.set_trace()
    print "pk entered" + pk

    if pk is not None:
        try:
            rdb.set_trace()
            d = Request.objects.filter(request_id=pk).update(status=2, completed_at=timezone.now())
            rdb.set_trace()
            print "pkpkkp" + pk
            if d >= 1:
                print 'My request_id ' + pk + ' is complete'
        except Exception as e:
            print 'Something is wrong!!!! %s ' % e
