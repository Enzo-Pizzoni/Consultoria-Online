import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

conexao = mysql.connector.connect(
    host= os.getenv("MYSQL_HOST"),
    user= os.getenv("MYSQL_USER"),
    password= os.getenv("MYSQL_PASSWORD"),
    database= os.getenv("MYSQL_DATABASE")
)

cursor = conexao.cursor()

cursor.close()
conexao.close() 