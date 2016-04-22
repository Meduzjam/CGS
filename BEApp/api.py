from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from BEApp.models import Car,Driver


class CarResource(ModelResource):
    class Meta:
        queryset = Car.objects.all()
        resource_name = 'Car'
        authentication = BasicAuthentication()

class DriverResource(ModelResource):
    class Meta:
        queryset = Driver.objects.all()
        resource_name = 'Driver'
        authentication = BasicAuthentication()
