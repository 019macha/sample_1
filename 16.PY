import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mcs019*",
  database="mymcs"
) 
mycursor = mydb.cursor()

mycursor.execute ("CREATE TABLE T2 (slno int not null, num INT NOT NULL)")