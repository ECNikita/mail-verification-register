from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Order_ticketdetailsModels import Order_ticketdetailsModel


def get_all_Order_ticket_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Ticket_id", "Order_id", "Customerticket_no", "Producerticket_no", "Notification" FROM public."Order_ticketdetails"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Order_ticketdetailsModel(row[0], row[1],row[2],row[3],row[4])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Order_id"],data["Customerticket_no"],data["Producerticket_no"],data["Notification"],data["Ticket_id"]]
        cursor.execute('UPDATE public."Order_ticketdetails" SET "Order_id"=%s, "Customerticket_no"=%s, "Producerticket_no"=%s, "Notification"=%s WHERE "Ticket_id"=%s', updatedata)

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
        updatedata = [data["Order_id"],data["Customerticket_no"],data["Producerticket_no"],data["Notification"]]
        cursor.execute('INSERT INTO public."Order_ticketdetails"("Order_id", "Customerticket_no", "Producerticket_no", "Notification") VALUES (%s,%s,%s,%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Order_ticketdetails" WHERE "Ticket_id"=%s', [P_id])

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
        cursor.execute('SELECT "Ticket_id" FROM public."Order_ticketdetails" WHERE "Ticket_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
