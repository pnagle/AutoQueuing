from AutoQueuing.celeryapp import app as celery
from DriverApp.models import Request
from django.utils import timezone


@celery.task
def update_ongoing_request(pk):
    if pk is not None:
        try:
            d = Request.objects.filter(request_id=pk).update(status=2, completed_at=timezone.now())
            if d >= 1:
                print 'My request_id ' + pk + ' is complete'
        except Exception as e:
            print 'Something is wrong!!!! %s ' % e
