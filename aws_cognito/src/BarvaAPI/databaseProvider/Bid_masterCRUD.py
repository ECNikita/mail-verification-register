from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Bid_masterModels import Bid_masterModel


def get_all_bid_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Bidtype_id", "Bidtype_name"	FROM public."Bid_master"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Bid_masterModel(row[0], row[1])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Bidtype_name"],data["Bidtype_id"]]
        cursor.execute('UPDATE public."Bid_master"	SET "Bidtype_name"=%s	WHERE "Bidtype_id"=%s', updatedata)

        connection.commit()
        
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False


def insertdetails(trad_data):
    cursor = connection.cursor()
    
    try:
        updatedata = [trad_data["Bidtype_name"]]
        cursor.execute('INSERT INTO public."Bid_master"( "Bidtype_name") VALUES (%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Bid_master" WHERE "Bidtype_id"=%s', [P_id])

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
        cursor.execute('SELECT "Bidtype_id" FROM public."Bid_master" WHERE "Bidtype_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
