from django.db import connection
from trade_details.views import *
from trade_details.models import Trade_detailsModel

def get_all_trade_details():
    cursor = connection.cursor()
    trade_List=[]
    try:
        #cursor.execute('SELECT "Trade_id", "Product_id", uid, "Date", "Quantity", "Price" FROM public."Trade_details" WHERE public."Trade_details"."Product_id" = %s ',[uid])
        cursor.execute('SELECT "Trade_id", "Product_id", uid, "Date", "Quantity", "Price" FROM public."Trade_details"')
        result_set = cursor.fetchall()
        for row in result_set:
            trade=Trade_detailsModel(row[0],row[1],row[2],row[3],row[4],row[5])
            trade_List.append(trade)
            
    finally:
        cursor.close()
    return trade_List

def insertdetails(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["Product_id"],data["uid"],data["Date"],data["Quantity"],data["Price"]]
        cursor.execute('INSERT INTO public."Trade_details"( "Product_id", uid, "Date", "Quantity", "Price")VALUES ( %s, %s, %s, %s, %s)',updatedata)
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def Validate_user_details(uuid):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT "Trade_id" FROM public."Trade_details" WHERE public."Trade_details"."Trade_id" = %s  ',[uuid])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None

def updatedetails(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["Product_id"],data["uid"],data["Date"],data["Quantity"],data["Price"],data["Trade_id"]]
        cursor.execute('UPDATE public."Trade_details" SET  "Product_id"=%s, uid=%s, "Date"=%s, "Quantity"=%s, "Price"=%s WHERE "Trade_id"=%s',updatedata)

        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False


def deletedetails(uid):
    cursor = connection.cursor()
    
    try:
        
        cursor.execute('DELETE FROM public."Trade_details" WHERE "Trade_id"=%s',[uid])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False