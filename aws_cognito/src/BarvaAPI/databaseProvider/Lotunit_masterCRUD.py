from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Lotunit_masterModels import Lotunit_masterModel


def get_all_Lot_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Lotunit_id", "Lotunit_name"	FROM public."Lotunit_master"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Lotunit_masterModel(row[0], row[1])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Lotunit_name"],data["Lotunit_id"]]
        cursor.execute('UPDATE public."Lotunit_master" SET  "Lotunit_name"=%s	WHERE "Lotunit_id"=%s', updatedata)

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
        updatedata = [data["Lotunit_name"]]
        cursor.execute('INSERT INTO public."Lotunit_master"( "Lotunit_name") VALUES (%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Lotunit_master" WHERE "Lotunit_id"=%s', [P_id])

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
        cursor.execute('SELECT "Lotunit_id" FROM public."Lotunit_master" WHERE "Lotunit_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
