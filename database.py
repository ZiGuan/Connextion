import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd= "0000",
  database="python_mysql"
)

mycursor = mydb.cursor()

sql = "INSERT INTO worktype (type1) VALUES (%s)"
val = ("personality_dichotomy")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")