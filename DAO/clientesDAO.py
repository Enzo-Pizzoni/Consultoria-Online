import models.clientes
from ConnectionFactory.ConnectionFactory import criar_conexao

#CREATE
def adicionar_usuario():              #CORRIGIR POSSIVEIS ERROS
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            c = models.clientes.Cliente()   
            comando = f'INSERT INTO clientes(nome, cpf, telefone, email) VALUES ({c.get_nome}, {c.get_cpf}, {c.get_telefone}, {c.get_email})' 
            cursor.execute(comando)
            conexao.commit()
            print(f"{cursor.rowcount} registro(s) atualizado(s).")

        except Exception as e:
            print("Erro ao adicionar:", e)
            conexao.rollback()

        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível se conectar ao banco.")

#READ
def visualizar_usuario():                      #AJUSTAR CÓDIGO
    conexao = criar_conexao()
    if conexao:
        try:
            #
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            resultados = cursor.fetchall()
            #
            for linha in resultados:
                print(linha)

        except Exception as e:
            print(" Erro ao executar consulta:", e)
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível se conectar ao banco.")

#UPDATE
def atualizar_nome():                      #AJUSTAR O CÓDIGO E ADICIONAR PARA CPF, TELEFONE, EMAIL
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            #
            sql = "UPDATE usuarios SET nome = %s WHERE id = %s"
            valores = ("Novo Nome", 1)
            #
            cursor.execute(sql, valores)
            conexao.commit()

            print(f"{cursor.rowcount} registro(s) atualizado(s).")

        except Exception as e:
            print("Erro ao atualizar:", e)
            conexao.rollback()

        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível se conectar ao banco.")

#REMOVE
def deletar_usuario():                      #AJUSTAR O CÓDIGO
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            #
            sql = "DELETE FROM usuarios WHERE id = %s" 
            valores = (1,)
            cursor.execute(sql, valores)
            conexao.commit()
            #
            print(f"{cursor.rowcount} registro(s) atualizado(s).")

        except Exception as e:
            print("Erro ao atualizar:", e)
            conexao.rollback()

        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível se conectar ao banco.")