from rest_framework.parsers import JSONParser 
from django.shortcuts import render,redirect
from product_details.models import Product_detailsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from product_details.serialize import ProductSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from product_details.databaseProvider.product_detailsCRUD import *
from django.http import JsonResponse
import json

@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    if request.method == 'GET':
        products = get_all_product_details()
        ProductSerializer = ProductSerialize(products, many=True)
        return JsonResponse(ProductSerializer.data, safe=False)
    
    elif request.method == 'POST':
        product_data = json.loads(request.body)
        valid_id =None
    
        if "Product_id" in product_data:
            valid_id = Validate_product_details(product_data["Product_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(product_data["Product_id"]):
            res= updatedetails(product_data)
        else:
        
            res = insertdetails(product_data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uid = request.query_params.get('Product_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


