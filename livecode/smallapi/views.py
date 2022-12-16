from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from smallapi.models import TwoNumberSum
from smallapi.serializers import TwoNumberSumSerializer


# Create your views here.
@api_view(["GET", "POST"])
def add(request):
    if request.method == "GET":
        two_number_sum_record = TwoNumberSum.objects.all()
        two_number_sum_serializer = TwoNumberSumSerializer(
            two_number_sum_record, many=True
        )
        return Response(two_number_sum_serializer.data)

    elif request.method == "POST":
        two_number_sum_record = TwoNumberSumSerializer(data=request.data)
        if two_number_sum_record.is_valid():
            two_number_sum_record.save()
            return Response(two_number_sum_record.data, status=status.HTTP_201_CREATED)
        return Response(
            two_number_sum_record.errors, status=status.HTTP_400_BAD_REQUEST
        )
