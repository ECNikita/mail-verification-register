from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.WarehouseModels import WarehouseModel
from decimal import Decimal

def get_all_warehouse_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Warehouse_id", "Warehouse_name", "Warehouse_address", "Warehouse_capacity", "Warehouse_geolocation" FROM public."Warehouse"')

        result_set = cursor.fetchall()
        
        for row in result_set:
            products =WarehouseModel(row[0],row[1],row[2],row[3],eval(row[4])[0],eval(row[4])[1])
            product_List.append(products)
            

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Warehouse_name"],data["Warehouse_address"],data["Warehouse_capacity"],Decimal(data["latitude"]),Decimal(data["longitude"]),data["Warehouse_id"]]
        cursor.execute("UPDATE public.\"Warehouse\" SET \"Warehouse_name\"=%s, \"Warehouse_address\"=%s, \"Warehouse_capacity\"=%s, \"Warehouse_geolocation\"='(%s,%s)' WHERE \"Warehouse_id\"=%s ", updatedata)

        connection.commit()
        
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False


def insertdetails(data):
    cursor = connection.cursor()
    try:
        updatedata = [data["Warehouse_name"],data["Warehouse_address"],data["Warehouse_capacity"],Decimal(data["latitude"]),Decimal(data["longitude"])]
        cursor.execute("INSERT INTO public.\"Warehouse\" (\"Warehouse_name\", \"Warehouse_address\", \"Warehouse_capacity\", \"Warehouse_geolocation\") VALUES (%s,%s,%s,'(%s,%s)')", updatedata)

        connection.commit()
        count = cursor.rowcount
        
        if count > 0:
            return True
    finally:
        cursor.close()
    return False


def deletedetails(P_id):
    cursor = connection.cursor()

    try:

        cursor.execute('DELETE FROM public."Warehouse" WHERE "Warehouse_id"=%s', [P_id])

        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False


def Validate_product_details(uuid):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT "Warehouse_id" FROM public."Warehouse" WHERE "Warehouse_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
