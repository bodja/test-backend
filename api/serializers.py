from rest_framework import serializers
from accounts.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'iban', 'photo', 'email')

    def save(self, **kwargs):
        kwargs['creator'] = self.context['request'].user
        return super(CustomerSerializer, self).save(**kwargs)