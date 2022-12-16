from rest_framework import serializers

from smallapi.models import TwoNumberSum


class TwoNumberSumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TwoNumberSum
        fields = ['id', 'first_num', 'second_num', 'sum']