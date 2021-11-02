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


class ProductGET(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Product_masterSerialize

    def get(self, request):
        prod_data = get_all_product_details()
        Product_masterSerializer = Product_masterSerialize(data=prod_data, many=True)
        Product_masterSerializer.is_valid()
        return JsonResponse(Product_masterSerializer.data, safe=False)


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
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class ProductUpdate(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Product_masterSerialize

    def put(self, request):
        product_data = JSONParser().parse(request)
        Product_masterSerializer = Product_masterSerialize(data=product_data)

        if Product_masterSerializer.is_valid() and "Product_id" in Product_masterSerializer.data:
            valid_id = Validate_product_details(Product_masterSerializer.data["Product_id"])
        res = False

        if valid_id is not None and int(valid_id) == int(Product_masterSerializer.data["Product_id"]):
            res = updatedetails(Product_masterSerializer.data)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(generics.CreateAPIView):
    serializer_class = Product_masterSerialize

    def delete(self, request):
        #product_data = JSONParser().parse(request)
        #Product_masterSerializer = Product_masterSerialize(data=product_data)

        uid = request.query_params.get('Product_id', None)

        res = False
        res = deletedetails(uid)

        if res is True:
            data = {"res": "True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res": "False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)
