from rest_framework_swagger import renderers
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.Models.Product_masterModels import *
from rest_framework.response import Response
from BarvaAPI.serializer.Product_masterSerialize import Product_masterSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Product_masterCRUD import *
from django.http import JsonResponse
import json
from rest_framework import status, permissions

class ProductInsert(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Product_masterSerialize
    def post(self, request):
        product_data = JSONParser().parse(request)
        Product_masterSerializer = Product_masterSerialize(data=product_data)
       
        if Product_masterSerializer.is_valid():
          res = insertdetails(Product_masterSerializer.data)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


# class DeleteProduct(generics.CreateAPIView):
#     def delete(self, request):
#         uid = request.query_params.get('Product_id', None)
        
#         res=False
#         res = deletedetails(uid)

#         if res is True:
#             data= {"res":"True"}
#             return JsonResponse((data), safe=False)
#         else :
#             data= {"res":"False"}
#             return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)