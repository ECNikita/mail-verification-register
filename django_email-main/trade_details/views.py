from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from trade_details.models import Trade_detailsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from trade_details.serialize import Trade_detailsSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from trade_details.databaseProvider.trade_detailsCRUD import *
from django.http import JsonResponse
import json


@api_view(['GET', 'POST', 'DELETE'])
def trade_list(request):
    if request.method == 'GET':
        trades = get_all_trade_details()

        uids = request.query_params.get('Trade_id', None)

        if uids is not None:
            for x in trades:
                if int(x.Trade_id) == int(uids):
                    trades = [x]
                    break

        Trade_detailsSerializer = Trade_detailsSerialize(trades, many=True)
        return JsonResponse(Trade_detailsSerializer.data, safe=False)

    elif request.method == 'POST':
        trade_data = json.loads(request.body)

        res = insertdetails(trade_data)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uid = request.query_params.get('Trade_id', None)
        print(uid)
        res = False
        res = deletedetails(uid)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)
