# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Email configuration
# sender_email = 'ravshanov709gmail.com'
# reciever_email = 'muhammadazizravshanov@gmail.com'
# subject = 'Account activation'
# message = f'Your activation code is: 1234'

# # SMTP server configuration for gmail
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_username = 'ravshanov709@gmail.com'
# smtp_password = 'hbjgugvbhjhvbjbh'

# # Create a multipart message and set headers
# email_message = MIMEMultipart()
# email_message['From'] = sender_email
# email_message['To'] = reciever_email
# email_message['Subject'] = subject

# email_message.attach(MIMEText(message, 'plain'))

# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.starttls()
#     server.login(smtp_username, smtp_password)

#     server.send_message(email_message)

# print('Success')

# def nums():
#     def filter(func):
#         with open('num.txt','r') as f:
#             data = f.readline()
#             for i in data.split():
#                 if i[:4]=='+998' and len(i)==13 and i[1:].isdigit():
#                     func(i)
#     return filter

# @nums()
# def save_nums(num):
#     with open('new_nums.txt','a') as f:
#         f.write(num + ',\n')



# def format_telefon_raqam(raqam: str) -> str:
#     if not raqam:
#         return "Telefon raqami berilmagan"

#     raqam = raqam.replace(" ", "").replace("-", "")

#     if len(raqam) != 12:
#         return "Noto'g'ri telefon raqami uzunligi"

#     kod = raqam[:3]
#     tugma = raqam[3:6]
#     qolgan = raqam[6:]

#     formatlangan_raqam = f"+{kod} ({tugma}) {qolgan[:2]}-{qolgan[2:4]}-{qolgan[4:]}"
#     return formatlangan_raqam

# telefon_raqam = "998907777"
# formatlangan_telefon_raqam = format_telefon_raqam(telefon_raqam)
# print(formatlangan_telefon_raqam)


# number = input("Iltimos, telefon raqamingizni kiriting: ")

# if number.startswith("+99890") or number.startswith("+99891") or number.startswith("+99890"):
#     print("Sizning raqamingiz Beeline operatoriga tegishli")
# elif number.startswith("+99893") or number.startswith("+99894") or number.startswith("+99897"):
#     print("Sizning raqamingiz Usell operatoriga tegishli")
# elif number.startswith("+99898") or number.startswith("+99899"):
#     print("Sizning raqamingiz Uzmobile operatoriga tegishli")
# else:
#     print("Kechirasiz, bizning bazamizda sizning kiritgan raqamingizga mos operator topilmadi")

# def operator_checker(func):
#     def wrapper(number):
#         if number.startswith("+99890") or number.startswith("+99891") or number.startswith("+99893"):
#             print("Sizning raqamingiz Ucell operatoriga tegishli")
#         elif number.startswith("+99893") or number.startswith("+99894") or number.startswith("+99897"):
#             print("Sizning raqamingiz Beeline operatoriga tegishli")
#         elif number.startswith("+99898") or number.startswith("+99899"):
#             print("Sizning raqamingiz Uzmobile operatoriga tegishli")
#         else:
#             print("Kechirasiz, bizning bazamizda sizning kiritgan raqamingizga mos operator topilmadi")
#         return func(number)
#     return wrapper
    
# @operator_checker
# def my_function(number):
#     # funksiya vazifalarini bajarish
#     return "Kodlar yozilayotganda, telefon raqami " + number + " operatoriga tegishli ekanligi aniqlandi"

# print(my_function("+998901234567"))



# import sqlite3
# conn = sqlite3.connect('dtb.db')

# cur = conn.cursor()
# cur.execute("""
#     create table if not exists'user'(
#         'first_name' varchar(50),
#         'lase_name' varchar(50),
#         'phone' varchar(13),
#         'birth_day' date,            
#         'is_active' boolean default false,
#         'size_of_shoes' int   
#     )
# """)
# conn.commit()

# # cur.execute("""
# #    insert into 'user'('first_name','lase_name','phone','birth_day','is_active','size_of_shoes')
# #    values
# #    ('Muhammadaziz','Ravshanov','+998888888888','2005-04-30',false,42),
# #    ('Sardor','Abrayov','+998974254585','2005-04-10',false,40) ,                          
# #    ('Nodir','Turgunov','+998997353577','2003-04-11',false,42)
# # """)
# # conn.commit()

# cur.execute("""
#     select phone from user where `first_name`='Muhammadaziz'
# """)
# rows =cur.fetchall()
# for row in rows:
#     print(row)

# conn.close()



# import sqlite3
# import hashlib

# def con():
#     conn = sqlite3.connect('dtb.db')
#     return conn

# def create_table_user():
#     conn =con()
#     cur =conn.cursor()
#     cur.execute(""" 
#         create table if not exists user(
#             `id` int not null primary key,
#             `first_name` varchar(30),
#             `last_name` varchar(30),
#             `email` varchar(50),           
#             `username` varchar(50),
#             `password` varchar(150),
#             `is_active` boolen default false,
#             `registered_datatime` datatime                
#         )
#     """)
#     conn.commit()
#     conn.close()


# def insert_user(data: dict):
#     conn=con()

#     cur = conn.cursor()
#     query= """
#         insert into user(
#             `first_name`,
#             `last_name`,
#             `email`,
#             `username`,
#             `password`,
#             `registered_datatime`
#             ) 
#             values(?,?,?,?,?,?)
#         """

# values=()





# import sqlite3
# import hashlib

# def con():
#     conn=sqlite3.connect('dtb.db')
#     return conn

# def create_table_user():
#     conn=con()
#     cur=conn.cursor()
#     cur.execute("""
#     create table if not exists `user`(
#                 `id` int not null primary key autoincrement,
#                 `first_name` varchar(20),
#                 `last_name` varchar(20),
#                 `email` varchar(50),
#                 `username` varchar(50),
#                 `password` varchar(150),
#                 `is_active` boolean default False,
#                 `registr_datetime` datetime
#         )
#     """)
#     conn.commit()
#     conn.close()

# def insert_user(data: dict):
#     conn=con()
#     aziz001 = hashlib.sha256()
#     aziz001.update(data['password1'].encode('utf-8'))
#     hashed_password = aziz001.hexdigest()
#     cur= conn.cursor()
#     query = """
#         insert into user(
#             `first_name`
#             `last_name`
#             `email`
#             `username`
#             `password`
#             `registr_datetime`
#         )
#         values = (?,?,?,?,?,?)
#     """
#     values = (data['first_name'], data['last_name'], data['email'], data['username'], hashed_password, data['registr_datetime'])
#     if data['password'] == data['password2']
    
    
# def is_exists(field ,field_data):
#     query= f"""


# """

# import sqlite3
# import hashlib
# from datetime import datetime

# def con():
#     conn = sqlite3.connect('dtb.db')
#     return conn

# def create_table_user():
#     conn = con()
#     cur = conn.cursor()
#     cur.execute("""
#         create table if not exists user(
#             `id` integer not null primary key autoincrement,
#             `first_name` varchar(30),
#             `last_name` varchar(30),
#             `email` varchar(50),
#             `username` varchar(50),
#             `password` varchar(150),
#             `is_active` boolean default false,
#             `registered_datetime` datetime
#         )
#     """)
#     conn.commit()
#     conn.close()


# def insert_user(data: dict):
#     conn = con()
#     cur = conn.cursor()
#     sha256 = hashlib.sha256()
#     sha256.update(data['password1'].encode('utf-8'))
#     hashed_password = sha256.hexdigest()
#     query = """
#         insert into user(
#             `first_name`,
#             `last_name`,
#             `email`,
#             `username`,
#             `password`,
#             `registered_datetime`
#         ) values (?, ?, ?, ?, ?, ?)
#     """
#     values = (data['first_name'], data['last_name'], data['email'], data['username'], hashed_password, datetime.now())
#     if data['password1'] == data['password2']:
#         if is_exist('username', data['username']):
#             print('This username is already exists!!!')
#             return 405
#         if is_exist('email', data['email']):
#             print('This email is already exists!!!')
#             return 405
#         cur.execute(query, values)
#         conn.commit()
#         conn.close()
#         return 201
#     else:
#         print('Passwords are not same!!!')
#         return 405


# # def login(data: dict):
# #     username = data['username']
# #     password = data['password']

# #     conn = con()
# #     cur = conn.cursor()
# #     sha256 = hashlib.sha256()
# #     sha256.update(password.encode('utf-8'))
# #     hashed_password = sha256.hexdigest()

# #     query = """
# #         select id from user where username=? and password=?
# #     """
# #     values = (username, hashed_password)
# #     cur.execute(query, values)
# #     dt = cur.fetchone()
# #     conn.close()
# #     return bool(dt)




# def is_exist(field, field_data):
#     query = f"""
#         select count(id) from user where {field}=?
#     """
#     value = (field_data,)
#     conn = con()
#     cur = conn.cursor()
#     cur.execute(query, value)
#     return cur.fetchone()[0]



import sqlite3
import hashlib
from datetime import datetime

def con():
    conn = sqlite3.connect('dtb.db')
    return conn

def create_table_user():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists user(
            `id` integer not null primary key autoincrement,
            `first_name` varchar(30),
            `last_name` varchar(30),
            `email` varchar(50),
            `username` varchar(50),
            `password` varchar(150),
            `is_active` boolean default false,
            `registered_datetime` datetime
        )
    """)
    conn.commit()
    conn.close()



def insert_user(data: dict):
    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(data['password1'].encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        insert into user(
            `first_name`,
            `last_name`,
            `email`,
            `username`,
            `password`,
            `registered_datetime`
        ) values (?, ?, ?, ?, ?, ?)
    """
    values = (data['first_name'], data['last_name'], data['email'], data['username'], hashed_password, datetime.now())
    if data['password'] == data['password1']:
        if is_exist('username', data['username']):
            print('This username is already exists!!!')
            return 405
        if is_exist('email', data['email']):
            print('This email is already exists!!!')
            return 405
        cur.execute(query, values)
        conn.commit()
        conn.close()
        return 201
    else:
        print('Passwords are not same!!!')
        return 405


def login(data: dict):
    username = data['username']
    password = data['password']

    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()

    query = """
        select id from user where username=? and password=?
    """
    values = (username, hashed_password)
    cur.execute(query, values)
    dt = cur.fetchone()
    conn.close()
    return bool(dt)


def is_exist(field, field_data):
    query = f"""
        select count(id) from user where {field}=?
    """
    value = (field_data,)
    conn = con()
    cur = conn.cursor()
    cur.execute(query, value)
    return cur.fetchone()[0]


def activate_user(data: dict):
    username = data['username']

    conn = con()
    cur = conn.cursor()

    query = """
        update user
        set is_active=true where username=?
    """
    values = (username,)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    return 200