from rest_framework import serializers

from api.models import account


class accountSerializer(serializers.ModelSerializer):

    class Meta:
        model = account
        fields = ('__all__')