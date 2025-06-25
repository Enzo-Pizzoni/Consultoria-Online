import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host= os.getenv("MYSQL_HOST"),
            user= os.getenv("MYSQL_USER"),
            password= os.getenv("MYSQL_PASSWORD"),
            database= os.getenv("MYSQL_DATABASE")
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida!")
            return conexao
    except Error as erro:
        print("Erro ao conectar ao banco de dados:")
        print(erro)
        return None