from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Producer_calculationSerialize import ProducerCalSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Producer_calculationCRUD import *
from django.http import JsonResponse


class ProducerCalGet(generics.CreateAPIView):
    serializer_class = ProducerCalSerialize
    def get(self, request):
        prod_data = get_all_producer_calc()
        ProducerCalSerializer = ProducerCalSerialize(data=prod_data, many=True)
        ProducerCalSerializer.is_valid()
        return JsonResponse(ProducerCalSerializer.data, safe=False)
