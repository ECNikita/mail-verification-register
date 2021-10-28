from django.db import connection
from register_details.views import *
from register_details.models import Register_details


def get_all_register_details():
    cursor = connection.cursor()
    register_List=[]
    try:
        cursor.execute('SELECT "Register_id", uid, "Firstname", "Lastname", "Address", "City", "State", "Zip", "Company", "CompanyAddress", "Phoneno" FROM public."Register_details" ')
        
        result_set = cursor.fetchall()
        for row in result_set:
            register=Register_details(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
            register_List.append(register)
            
    finally:
        cursor.close()
    return register_List

def updatedetails(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["Firstname"],data["Lastname"],data["Address"],data["City"],data["State"],data["Zip"],data["Company"],data["CompanyAddress"],data["Phone_no"],data["UserId"]]
        cursor.execute('UPDATE public."Register_details" SET "Firstname"=%s, "Lastname"=%s, "Address"=%s, "City"=%s, "State"=%s, "Zip"=%s, "Company"=%s, "CompanyAddress"=%s, "Phoneno"=%s WHERE public."Register_details"."UserId" =%s;',updatedata)

        
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
        updatedata = [data["UserId"],data["Firstname"],data["Lastname"],data["Address"],data["City"],data["State"],data["Zip"],data["Company"],data["CompanyAddress"],data["Phone_no"]]
        cursor.execute('INSERT INTO public."Register_details"("UserId","Firstname", "Lastname", "Address", "City", "State", "Zip", "Company", "CompanyAddress", "Phoneno") VALUES ( %s,%s,%s, %s, %s, %s, %s, %s, %s, %s)',updatedata)
        
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
        cursor.execute('SELECT "UserId" FROM public."Register_details" WHERE public."Register_details"."UserId" = %s  ',[uuid])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None

def deletedetails(uid):
    cursor = connection.cursor()
    
    try:
        
        cursor.execute('DELETE FROM public."Register_details"WHERE "UserId"=%s',[uid])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False