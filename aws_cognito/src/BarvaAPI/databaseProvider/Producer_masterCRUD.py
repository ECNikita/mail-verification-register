from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Producer_masterModels import Producer_masterModel


def get_all_product_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Producer_id", "Producer_name", "Producer_address", "Producer_mobileno", "Producer_adhaarno", "Producer_email", "Producer_pancard", "Producer_firmregistration", "Producer_gstno" FROM public."Producer_master"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Producer_masterModel(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Producer_name"], data["Producer_address"],data["Producer_mobileno"],data["Producer_adhaarno"], data["Producer_email"],data["Producer_pancard"],data["Producer_firmregistration"],data["Producer_gstno"],data["Producer_id"]]
        cursor.execute('UPDATE public."Producer_master"	SET "Producer_name"=%s, "Producer_address"=%s, "Producer_mobileno"=%s, "Producer_adhaarno"=%s, "Producer_email"=%s, "Producer_pancard"=%s, "Producer_firmregistration"=%s, "Producer_gstno"=%s WHERE "Producer_id"=%s', updatedata)

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
        updatedata = [data["Producer_name"], data["Producer_address"],data["Producer_mobileno"],data["Producer_adhaarno"], data["Producer_email"],data["Producer_pancard"],data["Producer_firmregistration"],data["Producer_gstno"]]
        cursor.execute('INSERT INTO public."Producer_master"( "Producer_name", "Producer_address", "Producer_mobileno", "Producer_adhaarno", "Producer_email", "Producer_pancard", "Producer_firmregistration", "Producer_gstno") VALUES (%s, %s, %s,%s,%s,%s,%s,%s)', updatedata)

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

        cursor.execute('DELETE FROM public."Producer_master" WHERE "Producer_id"=%s', [P_id])

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
        cursor.execute('SELECT "Producer_id" FROM public."Producer_master" WHERE "Producer_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
