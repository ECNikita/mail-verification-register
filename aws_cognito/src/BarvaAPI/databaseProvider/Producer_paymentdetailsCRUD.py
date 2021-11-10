from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Producer_paymentdetailsModels import Producer_paymentdetailsModel


def get_all_Producer_payment_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Customer_commisionpay_id", "Request_id", "Register_id", "Payment_date", "Payment_amount", "Wallet_details" FROM public."Producer_paymentdetails"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Producer_paymentdetailsModel(row[0], row[1],row[2],row[3],row[4],row[5])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Request_id"],data["Register_id"],data["Payment_date"],data["Payment_amount"],data["Wallet_details"],data["Customer_commisionpay_id"]]
        cursor.execute('UPDATE public."Producer_paymentdetails" SET "Request_id"=%s, "Register_id"=%s, "Payment_date"=%s, "Payment_amount"=%s, "Wallet_details"=%s WHERE "Customer_commisionpay_id"=%s', updatedata)

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
        updatedata = [data["Request_id"],data["Register_id"],data["Payment_date"],data["Payment_amount"],data["Wallet_details"]]
        cursor.execute('INSERT INTO public."Producer_paymentdetails"("Request_id", "Register_id", "Payment_date", "Payment_amount", "Wallet_details") VALUES (%s,%s,%s,%s,%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Producer_paymentdetails" WHERE "Customer_commisionpay_id"=%s', [P_id])

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
        cursor.execute('SELECT "Customer_commisionpay_id" FROM public."Producer_paymentdetails" WHERE "Customer_commisionpay_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
