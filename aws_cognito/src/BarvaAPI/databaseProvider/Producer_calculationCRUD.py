from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.Producer_calculationModels import ProducerCalModel


def get_all_producer_calc():
    cursor = connection.cursor()
    product_List = []
    try:
        
        cursor.execute('SELECT * from  public.producer_price()')

        result_set = cursor.fetchall()
        for row in result_set:
            products = ProducerCalModel(row[0],row[1],row[2])
            product_List.append(products)
            
            
    finally:
        cursor.close()
    return product_List