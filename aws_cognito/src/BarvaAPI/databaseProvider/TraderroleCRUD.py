from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.TraderroleModels import TraderroleModel


def get_all_traderrole_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Traderrole_id", "Traderrole_name" FROM public."Trade_role"')
        result = cursor.fetchall()
        
        for row in result:
            print(row[0])
            print(row[1])
            traderrole = TraderroleModel(row[0],row[1])
            print(traderrole)
            product_List.append(tr)
            

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Traderrole_name"],data["Traderrole_id"]]
        cursor.execute('UPDATE public."Trade_role"	SET "Traderrole_name"=%s	WHERE "Traderrole_id"=%s', updatedata)

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
        updatedata = [data["Traderrole_name"]]
        cursor.execute('INSERT INTO public."Trade_role" ("Traderrole_name") VALUES (%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Trade_role" WHERE "Traderrole_id"=%s', [P_id])

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
        cursor.execute('SELECT "Traderrole_id" FROM public."Trade_role" WHERE "Traderrole_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
