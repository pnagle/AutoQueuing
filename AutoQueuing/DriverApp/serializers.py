from rest_framework import serializers
from .models import Request, Customer


class RequestSerializer(serializers.ModelSerializer):

    request_location_lat = serializers.DecimalField(max_digits=15, decimal_places=11, required=False)
    request_location_long = serializers.DecimalField(max_digits=15, decimal_places=11, required=False)
    customer_id = serializers.SlugRelatedField(
        slug_field='customer_id',
        queryset=Customer.objects.all(),
        required=False,
    )

    class Meta:
        model = Request
        fields = '__all__'
