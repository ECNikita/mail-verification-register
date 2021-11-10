from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Order_ticketdetailsSerialize import Order_ticketdetailsSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Order_ticketdetailsCRUD import *
from django.http import JsonResponse


class Order_ticket_detailsGET(generics.CreateAPIView):
    serializer_class = Order_ticketdetailsSerialize
    def get(self, request):
        ord_ticket_data = get_all_Order_ticket_details()
        Order_ticketdetailsSerializer = Order_ticketdetailsSerialize(data=ord_ticket_data, many=True)
        Order_ticketdetailsSerializer.is_valid()
        return JsonResponse(Order_ticketdetailsSerializer.data, safe=False)

class Order_ticket_detailsInsert(generics.CreateAPIView):
    serializer_class = Order_ticketdetailsSerialize
    def post(self, request):
        ord_ticket_data = JSONParser().parse(request)
        Order_ticketdetailsSerializer = Order_ticketdetailsSerialize(data=ord_ticket_data)
        res = False
        if Order_ticketdetailsSerializer.is_valid():
            res = insertdetails(Order_ticketdetailsSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class Order_ticket_detailsUpdate(generics.CreateAPIView):
    serializer_class = Order_ticketdetailsSerialize
    def put(self, request):
        ord_ticket_data = JSONParser().parse(request)
        Order_ticketdetailsSerializer = Order_ticketdetailsSerialize(data=ord_ticket_data)
       
        if Order_ticketdetailsSerializer.is_valid() and "Ticket_id" in Order_ticketdetailsSerializer.data:
            valid_id = Validate_product_details(Order_ticketdetailsSerializer.data["Ticket_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Order_ticketdetailsSerializer.data["Ticket_id"]):
            res= updatedetails(Order_ticketdetailsSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class Order_ticket_detailsDelete(generics.CreateAPIView):
    serializer_class = Order_ticketdetailsSerialize
    def delete(self, request):
        uid = request.query_params.get('Ticket_id', None)
        res=False
        res = deletedetails(uid)
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)