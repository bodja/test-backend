from rest_framework import serializers
from accounts.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'iban', 'photo')
