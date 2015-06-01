from rest_framework import serializers
from accounts.models import Customer
from api.fields import HyperlinkedFileField


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    photo_thumbnail = HyperlinkedFileField(source='thumbnail_2x3',
                                           read_only=True)
    photo_thumbnail_small = HyperlinkedFileField(source='thumbnail_small',
                                                 read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'iban', 'photo', 'email',
                  'photo_thumbnail', 'photo_thumbnail_small')

    def save(self, **kwargs):
        kwargs['creator'] = self.context['request'].user
        return super(CustomerSerializer, self).save(**kwargs)
