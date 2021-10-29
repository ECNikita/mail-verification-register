from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Product_pricebyproducerModels import Product_pricebyproducerModel


def get_all_product_price_details():
    cursor = connection.cursor()
    product_List = []
    try:
        cursor.execute('SELECT "Product_id", "Producer_id", price, datefrom, dateto, "Lotunit_id", quantity, "Serial_id"	FROM public."Product_PricebyProducer"')

        result_set = cursor.fetchall()
        for row in result_set:
            products = Product_pricebyproducerModel(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
            product_List.append(products)

    finally:
        cursor.close()
    return product_List


def updatedetails(data):
    cursor = connection.cursor()

    try:
        updatedata = [data["price"],data["datefrom"],data["dateto"],data["quantity"],data["Serial_id"]]
        cursor.execute('UPDATE public."Product_PricebyProducer"	SET  price=%s, datefrom=%s, dateto=%s, quantity=%s	WHERE "Serial_id"=%s', updatedata)

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
        updatedata = [data["Product_id"],data["Producer_id"],data["price"],data["datefrom"],data["dateto"],data["Lotunit_id"],data["quantity"]]
        cursor.execute('INSERT INTO public."Product_PricebyProducer"("Product_id", "Producer_id", price, datefrom, dateto, "Lotunit_id", quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)', updatedata)

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

        cursor.execute('DELETE FROM public."Product_PricebyProducer" WHERE "Serial_id"=%s', [P_id])

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
        cursor.execute('SELECT "Serial_id" FROM public."Product_PricebyProducer" WHERE "Serial_id"=%s  ', [uuid])

        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None
