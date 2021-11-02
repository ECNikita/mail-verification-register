from rest_framework_swagger import renderers
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.response import Response
from BarvaAPI.serializer.TraderroleSerialize import TraderroleSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.TraderroleCRUD import *
from django.http import JsonResponse
from rest_framework import status, permissions


class TraderroleGET(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = TraderroleSerialize

    def get(self, request):
       
        traderrole_data = get_all_traderrole_details()
        
        TraderroleSerializer = TraderroleSerialize(data=traderrole_data, many=True)
        TraderroleSerializer.is_valid()
        return JsonResponse(TraderroleSerializer.data, safe=False, many=True)


class TraderroleInsert(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = TraderroleSerialize

    def post(self, request):
        trader_data = JSONParser().parse(request)
        TraderroleSerializer = TraderroleSerialize(data=trader_data)
        res = False
        if TraderroleSerializer.is_valid():
            res = insertdetails(TraderroleSerializer.data)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class TraderroleUpdate(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = TraderroleSerialize

    def put(self, request):
        trader_data = JSONParser().parse(request)
        TraderroleSerializer = TraderroleSerialize(data=trader_data)

        if TraderroleSerializer.is_valid() and "Traderrole_id" in TraderroleSerializer.data:
            valid_id = Validate_product_details(
                TraderroleSerializer.data["Traderrole_id"])
        res = False

        if valid_id is not None and int(valid_id) == int(TraderroleSerializer.data["Traderrole_id"]):
            res = updatedetails(TraderroleSerializer.data)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class TraderroleDelete(generics.CreateAPIView):
    serializer_class = TraderroleSerialize

    def delete(self, request):
        #product_data = JSONParser().parse(request)
        #Product_masterSerializer = Product_masterSerialize(data=product_data)

        uid = request.query_params.get('Traderrole_id', None)

        res = False
        res = deletedetails(uid)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)
