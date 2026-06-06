import mysql.connector

connection = mysql.connector.connect(

host='localhost',

user='root',

password='D_18032005_s',

database='customer_segmentation_db'

)

print(

"SQL Connection Successful"

)
