from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.CustomerProducer_Bid_detailsModels import CustomerProducer_Bid_detailsModel


def get_all_Cust_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Request_id", "Producer_id", "Register_id", "Product_id", "Producerproductprice", "Customer_bidprice", "DateTime", "Bidtype_id", "Quantity", "Trader_notification", "Trader_approval", "Approval_comments" FROM public."CustomerProducer_Bid_details"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = CustomerProducer_Bid_detailsModel(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Producer_id"],data["Register_id"],data["Product_id"],data["Producerproductprice"],data["Customer_bidprice"],data["DateTime"],data["Bidtype_id"],data["Quantity"],data["Trader_notification"],data["Trader_approval"],data["Approval_comments"],data["Request_id"]]
        cursor.execute('UPDATE public."CustomerProducer_Bid_details" SET "Producer_id"=%s, "Register_id"=%s, "Product_id"=%s, "Producerproductprice"=%s, "Customer_bidprice"=%s, "DateTime"=%s, "Bidtype_id"=%s, "Quantity"=%s, "Trader_notification"=%s, "Trader_approval"=%s, "Approval_comments"=%s WHERE "Request_id"=%s', updatedata)

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
        updatedata = [data["Producer_id"],data["Register_id"],data["Product_id"],data["Producerproductprice"],data["Customer_bidprice"],data["DateTime"],data["Bidtype_id"],data["Quantity"],data["Trader_notification"],data["Trader_approval"],data["Approval_comments"]]
        cursor.execute('INSERT INTO public."CustomerProducer_Bid_details"("Producer_id", "Register_id", "Product_id", "Producerproductprice", "Customer_bidprice", "DateTime", "Bidtype_id", "Quantity", "Trader_notification", "Trader_approval", "Approval_comments") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', updatedata)

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

        cursor.execute('DELETE FROM public."CustomerProducer_Bid_details" WHERE "Request_id"=%s', [P_id])

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
        cursor.execute('SELECT "Request_id" FROM public."CustomerProducer_Bid_details" WHERE "Request_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
