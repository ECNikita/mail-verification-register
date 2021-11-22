from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.BiddingforProductSerialize import BidProductSerialize,BidCalSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.BiddingforProductCRUD import *
from django.http import JsonResponse


class BiddingCalc(generics.CreateAPIView):
    serializer_class = BidProductSerialize
    def post(self, request):
        Bid_data = JSONParser().parse(request)
        BidProductSerializer = BidProductSerialize(data=Bid_data)
        res = False
        res=[]
        if BidProductSerializer.is_valid():
           res = get_all_bid_calc(BidProductSerializer.data)
           
        BidCalSerializer= BidCalSerialize(data=res, many=True)
        BidCalSerializer.is_valid()
        return JsonResponse(BidCalSerializer.data, safe=False)  