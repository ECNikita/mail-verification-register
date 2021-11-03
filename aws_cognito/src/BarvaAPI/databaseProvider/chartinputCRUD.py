from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.chartinputModels import *

def get_all_chart_quan_details(ChartModel):
    cursor = connection.cursor()
    product_List = []
    
    try:
        updatedata = [ChartModel["Product_id"],ChartModel["datefrom"],ChartModel["dateto"]]
        cursor.execute('SELECT price ,quantity, datefrom FROM public."Product_PricebyProducer" WHERE "Product_id"=%s and "datefrom">=%s and "dateto"<=%s ',updatedata)
        result_set = cursor.fetchall()
        for row in result_set:
            products = ChartResponseModel(row[0],row[1],row[2])
            product_List.append(products)
            

    finally:
        cursor.close()
    return product_List
