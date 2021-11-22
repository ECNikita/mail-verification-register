from django.db import connection
from BarvaAPI.view import *
from BarvaAPI.Models.BiddingforProductModels import BidProductModel,BidCalModel


def get_all_bid_calc(data):
    cursor = connection.cursor()
    product_List = []
    try:
        updatedata = [data["startdate"],data["todate"]]
        cursor.execute('SELECT *  from public.bid_calc(%s,%s)',updatedata)

        result_set = cursor.fetchall()
        for row in result_set:
            products = BidCalModel(row[0],row[1],row[2])
            product_List.append(products)
            
            
    finally:
        cursor.close()
    return product_List
