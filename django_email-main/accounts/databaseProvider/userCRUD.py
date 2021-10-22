from django.db import connection
from accounts.models import Profile

def Validate_user(email,password):
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT "Email","Password","IsActive" FROM public."User" WHERE public."User"."Email" = %s and public."User"."Password"=%s ',[email,password])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return {"Email":row[0],"Password":row[1],"IsActive":row[2]}
    finally:
        cursor.close()
    return None

def Register_user(email,password,otp):
    cursor = connection.cursor()
    
    try:
        cursor.execute('INSERT INTO public."User"("Email", "Password", otp,"IsActive")	VALUES (%s, %s, %s, %s); ',[email,password,otp,"0"])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
        
    finally:
        cursor.close()
    return False

def Verify_user(email,otp):
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT "Email" FROM public."User" WHERE public."User"."Email" = %s and public."User".otp=%s ',[email,otp])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return True
    finally:
        cursor.close()
    return False

def Activate_user(email):
    cursor = connection.cursor()
    
    try:
        cursor.execute('UPDATE public."User" SET "IsActive"=%s WHERE public."User"."Email" = %s ',["1",email])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def Check_user_already_register(email):
    cursor = connection.cursor()
    
    try:
        print("Check_user_already_register")
        cursor.execute('SELECT "Email" FROM public."User" WHERE public."User"."Email" = %s ',[email])
        
        result_set = cursor.fetchall()
        print(result_set)
        for row in result_set:
            return True
    finally:
        cursor.close()
    return False

def user_all():
    cursor = connection.cursor()
    user_all = [] 
    try:
        cursor.execute('SELECT uid, "Email", "Password", "IsActive", otp FROM public."User"')
        
        result_set = cursor.fetchall()
        for row in result_set:
            users =Profile(row[0],row[1],row[2],row[3],row[4])
            user_all.append(users)
    finally:
        cursor.close()
    return user_all

def user_delete(uid):
    cursor = connection.cursor()
    try:
        cursor.execute('DELETE FROM public."User" WHERE uid = %s',[uid])
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def user_update(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["Email"],data["Password"],data["uid"]]
        cursor.execute('UPDATE public."User" SET  "Email"=%s, "Password"=%s WHERE uid =%s;',updatedata)

        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def user_insert(data,otp):
    cursor = connection.cursor()
    
    try:
        update =[data["Email"],data["Password"],"0",otp]
        cursor.execute('INSERT INTO public."User"( "Email", "Password", "IsActive", otp) VALUES ( %s, %s,%s,%s);',update)
        
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
        cursor.execute('SELECT uid FROM public."User" where uid=%s ',[uuid])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None