from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from serializers import RequestSerializer
from rest_framework import permissions
from .models import Request, Driver, Customer
from rest_framework import mixins
from rest_framework import generics


def index(request):
    driverid = request.GET.get('id', None)
    latest_request_list = Request.objects.order_by('-requested_at')
    template = loader.get_template('DriverApp/driverapp.html')
    context = {
        'latest_request_list_waiting': latest_request_list.filter(status=0),
        'latest_request_list_ongoing': latest_request_list.filter(driver_id=driverid).filter(status=1),
        'latest_request_list_complete': latest_request_list.filter(driver_id=driverid).filter(status=2),
        'driver_id': driverid,
    }
    if request.method == 'post':
        print 'here'
    return HttpResponse(template.render(context, request))


class RequestViewSet(viewsets.ModelViewSet):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.AllowAny,)


class request_list(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all ride requests, or create a new request.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class request_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a code request.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
