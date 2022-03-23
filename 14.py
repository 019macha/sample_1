import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mcs019*",
  database="mymcs"
)

mycursor = mydb.cursor()

sql = "INSERT INTO T1 (SLNO, id) VALUES (%s, %s)"
val = [
  ('1', '1'),
  ('2', '1'),
  ('3', '2'),
  ('4', '3'),
 ]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 