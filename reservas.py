import psycopg2

class Reservas_BD:
    def __init__(self):
        pass

    def abrir_coneccao(self):
        try:
            self.coneccao = psycopg2.connect(user = 'postgres', password = 'INSIRA-SUA-SENHA, host = '127.0.0.1', port = '5432', database = 'postgres')
            print('Conexão aberta')
        except (Exception, psycopg2.Error) as error:
            if (self.coneccao):
                print('Falha ao se conectar a banco de dados', error)

    def selecionar_dados(self):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_select_query = """select * from public."RESERVAS" order by "CODIGO" ASC"""
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

    def selecionar_dados_especificos(self, tipo_de_busca, busca):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_select_query2 = f"""SELECT * FROM public."RESERVAS" WHERE "{tipo_de_busca}" LIKE '%{busca}%' """
            cursor.execute(sql_select_query2)
            registro = cursor.fetchall()
            print(registro)

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print('Conexão Fechada')
        return registro

    def inserir_dados(self, codigo, descricao, nome, data_ret, data_dev, equipe, telefone):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_insert_query = """ INSERT INTO public."RESERVAS"("CODIGO", "DESCRICAO", "NOME", "DATA_RETIRADA", "DATA_DEVOLUCAO", "EQUIPE", "TELEFONE") VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (codigo, descricao, nome, data_ret, data_dev, equipe, telefone)
            cursor.execute(sql_insert_query, record_to_insert)
            self.coneccao.commit()
            print("Registro inserido com successo")

        except (Exception, psycopg2.Error) as error:
            print("Falha ao inserir registro", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def excluir_dados(self, codigo, data_retirada):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_delete_query = """Delete from public."RESERVAS" where "CODIGO" = %s and "DATA_RETIRADA" = %s"""
            cursor.execute(sql_delete_query, (codigo, data_retirada))
            self.coneccao.commit()
            print("Registro excluído com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")