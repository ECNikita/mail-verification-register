from django.db import connection
from uploadImageapp.views import *
from uploadImageapp.models  import UploadModel



def Insert_upload_doc(data):
    cursor = connection.cursor()
    
    try:
        update =[data["uid"],data["Pancard"],data["Aadhaarcard"],data["Companyid"],data["Photo"],data["Pancard_file"],data["Aadhaarcard_file"],data["Companyid_file"],data["Photo_file"]]
        cursor.execute('INSERT INTO public."Upload_documents"( "uid","Pancard", "Aadhaarcard", "Companyid", "Photo", "Pancard_file", "Aadhaarcard_file", "Companyid_file", "Photo_file")VALUES ( %s,%s, %s, %s, %s, %s, %s, %s, %s)',update)
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def Validate_user_detail(uuid):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT "uid" FROM public."Upload_documents" WHERE public."Upload_documents"."uid" = %s  ',[uuid])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None

def user_upload_doc():
    cursor = connection.cursor()
    upload_doc = [] 
    try:
        cursor.execute('SELECT  uid,"Pancard", "Aadhaarcard", "Companyid", "Photo", "Pancard_file", "Aadhaarcard_file", "Companyid_file", "Photo_file" FROM public."Upload_documents"')
        
        result_set = cursor.fetchall()
        for row in result_set:
            uploads =UploadModel(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            upload_doc.append(uploads)
    finally:
        cursor.close()
    return upload_doc

def Update_upload_doc(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["Pancard"],data["Aadhaarcard"],data["Companyid"],data["Photo"],data["Pancard_file"],data["Aadhaarcard_file"],data["Companyid_file"],data["Photo_file"],data["uid"]]
        cursor.execute('UPDATE public."Upload_documents" SET  "Pancard"=%s, "Aadhaarcard"=%s, "Companyid"=%s, "Photo"=%s, "Pancard_file"=%s, "Aadhaarcard_file"=%s, "Companyid_file"=%s, "Photo_file"=%s WHERE public."Upload_documents"."uid" =%s',updatedata)

        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False
    

def delete_details(uid):
    cursor = connection.cursor()
    
    try:
        
        cursor.execute('DELETE FROM public."Upload_documents" WHERE uid = %s',[uid])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False