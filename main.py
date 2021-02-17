import sqlite3
from os import system

conn = sqlite3.connect('sqlite.db')

name = input("Enter Your Name: ")
_class = input("In which Class do you Read: ")
school = input("What is Your School's/College's Name: ")
age = input("What's Your age: ")
passion = input("What's Your Passion: ")
parents = input("What's Name of Your Parents: ")
phone = input("What is your Permanent Mobile Numbe: ")
whatsapp = input("What's Your WhatsApp Number: ")
model = input("What's Your Mobile Phone's Model: ")
business = input("What's is Your Business: ")
area = input("From which area you belong to (rural/urban): ")

try:
    conn.execute('''
         CREATE TABLE PEOPLE(
         NAME           TEXT    NOT NULL,
         CLASS          TEXT    NOT NULL,
         SCHOOL         TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         PASSION        CHAR    NOT NULL,
         PARENTS        CHAR    NOT NULL,
         PHONE          INT(10) NOT NULL,
         WHATSAPP       INT(10) NOT NULL,
         MODEL          CHAR    NOT NULL,
         BUSINESS       TEXT    NOT NULL,
         AREA           TEXT    NOT NULL
         );''')
except:
    pass
conn.execute(f"INSERT INTO PEOPLE (NAME, CLASS, SCHOOL, AGE, PASSION, PARENTS, PHONE, WHATSAPP, MODEL, BUSINESS, AREA) \
      VALUES ('{name}', '{_class}', '{school}', '{age}', '{passion}', '{parents}', '{phone}', '{whatsapp}', '{model}', '{business}', '{area}')");



conn.commit()
system("clear")

cursor = conn.execute("SELECT NAME, CLASS, SCHOOL, AGE, PASSION, PARENTS, PHONE, WHATSAPP, MODEL, BUSINESS, AREA from people")
for row in cursor:
   print("Name = ", row[0])
   print("Class = ", row[1])
   print("School = ", row[2])
   print("Age = ", row[3])
   print("Passsion = ", row[4])
   print("Parents = ", row[5])
   print("Phone = ", row[6])
   print("WhatsApp = ", row[7])
   print("Model = ", row[8])
   print("Business = ", row[9])
   print("Area = ", row[10])
   print("=====================================\n\n")
conn.close()
