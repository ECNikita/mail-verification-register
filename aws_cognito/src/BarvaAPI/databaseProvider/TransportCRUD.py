from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.TransportModels import TransportModel
from decimal import Decimal

def get_all_transport_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Transport_id", "Transport_name", "Transport_address", "Transport_firmregistration", "Transport_frim_pancard", "Transport_geolocation" FROM public."Transport"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = TransportModel(row[0],row[1],row[2],row[3],row[4],eval(row[5])[0],eval(row[5])[1])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Transport_name"],data["Transport_address"],Decimal(data["latitude"]),Decimal(data["longitude"]),data["Transport_firmregistration"],data["Transport_frim_pancard"],data["Transport_id"]]
        cursor.execute("UPDATE public.\"Transport\" SET \"Transport_name\"=%s, \"Transport_address\"=%s, \"Transport_geolocation\"='(%s,%s)', \"Transport_firmregistration\"=%s, \"Transport_frim_pancard\"=%s WHERE \"Transport_id\"=%s", updatedata)

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
        updatedata = [data["Transport_name"],data["Transport_address"],Decimal(data["latitude"]),Decimal(data["longitude"]),data["Transport_firmregistration"],data["Transport_frim_pancard"]]
        cursor.execute("INSERT INTO public.\"Transport\" (\"Transport_name\", \"Transport_address\", \"Transport_geolocation\", \"Transport_firmregistration\",\"Transport_frim_pancard\") VALUES (%s,%s,'(%s,%s)',%s,%s)", updatedata)

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

        cursor.execute('DELETE FROM public."Transport" WHERE "Transport_id"=%s', [P_id])

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
        cursor.execute('SELECT "Transport_id" FROM public."Transport" WHERE "Transport_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
