from django.db import connection
from BarvaAPI.view.registerViews import *
from BarvaAPI.Models.registerModels import Register_details


def get_all_register_details():
    cursor = connection.cursor()
    register_List=[]
    try:
        cursor.execute('SELECT "Register_id", "UserId", "Firstname", "Lastname", "Address", "City", "State", "Zip", "Firm", "Firm_pan", "Phoneno","Gst_no", "Credit_limit", "Registration_date", "Wallet", geolocation FROM public."Customer_info" ')
        
        result_set = cursor.fetchall()
        for row in result_set:
            register=Register_details(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],eval(row[15])[0],eval(row[15])[1])
            register_List.append(register)
            
    finally:
        cursor.close()
    return register_List

def updatedetails(data):
    cursor = connection.cursor()
    try:
        updatedata = [data["Firstname"],data["Lastname"],data["Address"],data["City"],data["State"],data["Zip"],data["Firm"],data["Firm_pan"],data["Phoneno"],data["Gst_no"],data["Credit_limit"],data["Registration_date"],data["Wallet"],data["latitude"],data["longitude"],data["Register_id"]]
        cursor.execute("UPDATE public.\"Customer_info\" SET \"Firstname\"=%s, \"Lastname\"=%s, \"Address\"=%s, \"City\"=%s, \"State\"=%s, \"Zip\"=%s, \"Firm\"=%s, \"Firm_pan\"=%s, \"Phoneno\"=%s ,\"Gst_no\"=%s, \"Credit_limit\"=%s, \"Registration_date\"=%s, \"Wallet\"=%s , \"geolocation\"='(%s,%s)' WHERE \"Register_id\" =%s",updatedata)

        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def insertdetails(data,user_id):
    cursor = connection.cursor()
    
    try:
        updatedata = [user_id,data["Firstname"],data["Lastname"],data["Address"],data["City"],data["State"],data["Zip"],data["Firm"],data["Firm_pan"],data["Phoneno"],data["Gst_no"],data["Credit_limit"],data["Registration_date"],data["Wallet"],data["latitude"],data["longitude"]]
        cursor.execute("INSERT INTO public.\"Customer_info\" (\"UserId\",\"Firstname\", \"Lastname\", \"Address\", \"City\", \"State\", \"Zip\", \"Firm\", \"Firm_pan\", \"Phoneno\" ,\"Gst_no\", \"Credit_limit\", \"Registration_date\", \"Wallet\" , \"geolocation\") VALUES ( %s,%s,%s, %s, %s, %s, %s, %s, %s, %s ,%s,%s,%s,%s,'(%s,%s)')",updatedata)
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def Validate_user_details(uuid):
    cursor = connection.cursor()
    
    print(uuid)
    try:
        cursor.execute('SELECT  "Register_id" FROM public."Customer_info" WHERE "Register_id"=%s',[uuid])
        
        result_set = cursor.fetchall()
        
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None

def deletedetails(uid):
    cursor = connection.cursor()
    
    try:
        
        cursor.execute('DELETE FROM public."Customer_info"WHERE "Register_id" = %s',[uid])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False