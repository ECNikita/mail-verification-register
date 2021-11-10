from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Order_detailsModels import Order_detailsModel


def get_all_Order_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Order_id", "Customer_commisionpay_id", "Request_id", "Order_date", "Order_price" FROM public."Order_details"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Order_detailsModel(row[0], row[1],row[2],row[3],row[4])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Customer_commisionpay_id"],data["Request_id"],data["Order_date"],data["Order_price"],data["Order_id"]]
        cursor.execute('UPDATE public."Order_details" SET "Customer_commisionpay_id"=%s, "Request_id"=%s, "Order_date"=%s, "Order_price"=%s WHERE "Order_id"=%s', updatedata)

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
        updatedata = [data["Customer_commisionpay_id"],data["Request_id"],data["Order_date"],data["Order_price"]]
        cursor.execute('INSERT INTO public."Order_details"("Customer_commisionpay_id", "Request_id", "Order_date", "Order_price") VALUES (%s,%s,%s,%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Order_details" WHERE "Order_id"=%s', [P_id])

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
        cursor.execute('SELECT "Order_id" FROM public."Order_details" WHERE "Order_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
