from django.db import connection
from product_details.views import *
from product_details.models import Product_detailsModel


def get_all_product_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Product_id", "Product_name", "Product_size", "Product_price" FROM public."Product_details"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Product_detailsModel(row[0], row[1], row[2], row[3])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["Product_name"], data["Product_size"],
                      data["Product_price"], data["Product_id"]]
        cursor.execute('UPDATE public."Product_details"	SET "Product_name"=%s, "Product_size"=%s, "Product_price"=%s WHERE "Product_id"=%s', updatedata)

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
        updatedata = [ data["Product_name"],data["Product_size"], data["Product_price"]]
        cursor.execute('INSERT INTO public."Product_details"( "Product_name", "Product_size", "Product_price") VALUES (%s, %s, %s);', updatedata)

        connection.commit()
        print("after insert")
        count = cursor.rowcount
        print(count)
        if count > 0:
            return True
    finally:
        cursor.close()
    return False


def deletedetails(P_id):
    cursor = connection.cursor()

    try:

        cursor.execute('DELETE FROM public."Product_details" WHERE "Product_id"=%s', [P_id])

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
        cursor.execute(
            'SELECT "Product_id" FROM public."Product_details" WHERE "Product_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
