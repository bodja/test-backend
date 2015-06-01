from rest_framework import serializers


class HyperlinkedFileField(serializers.FileField):
    def to_representation(self, value):
        request = self.context.get('request', None)
        if request:
            return request.build_absolute_uri(value.url)
        return value
