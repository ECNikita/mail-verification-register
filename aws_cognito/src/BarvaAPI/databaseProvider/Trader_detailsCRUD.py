from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Trader_detailsModels import Trader_detailsModel


def get_all_trader_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Trader_id", "Traderrole_id", "Trader_name", "Trader_email", "Trader_mobile" FROM public."Trader_details"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Trader_detailsModel(row[0],row[1],row[2],row[3],row[4])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Traderrole_id"],data["Trader_name"],data["Trader_email"],data["Trader_mobile"],data["Trader_id"]]
        cursor.execute('UPDATE public."Trader_details"	SET  "Traderrole_id"=%s, "Trader_name"=%s, "Trader_email"=%s, "Trader_mobile"=%s WHERE "Trader_id"=%s', updatedata)

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
        updatedata = [data["Traderrole_id"],data["Trader_name"],data["Trader_email"],data["Trader_mobile"]]
        cursor.execute('INSERT INTO public."Trader_details"("Traderrole_id", "Trader_name", "Trader_email", "Trader_mobile") VALUES (%s,%s,%s,%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Trader_details" WHERE "Trader_id"=%s', [P_id])

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
        cursor.execute('SELECT "Trader_id" FROM public."Trader_details" WHERE "Trader_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
