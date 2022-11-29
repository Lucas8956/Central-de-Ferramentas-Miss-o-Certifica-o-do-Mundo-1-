import psycopg2

class Tecnicos_BD:
    def abrir_coneccao(self):
        try:
            self.coneccao = psycopg2.connect(user = 'postgres', password = 'INSIRA-SUA-SENHA', host = '127.0.0.1', port = '5432', database = 'postgres')
            print('Coneção aberta')

        except (Exception, psycopg2.Error) as error:
            if (self.coneccao):
                print('Falha ao se conectar a banco de dados', error)

    def selecionar_dados(self):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_select_query = """select * from public."Tecnicos" order by "CPF" ASC"""
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
            sql_select_query2 = f"""SELECT * FROM public."Tecnicos" WHERE "{tipo_de_busca}" LIKE '%{busca}%' order by "CPF" ASC """
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

    def inserir_dados(self, cpf, nome, telefone, turno, equipe):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_insert_query = """ INSERT INTO public."Tecnicos"("CPF", "NOME", "TELEFONE", "TURNO", "EQUIPE") VALUES (%s, %s, %s, %s, %s)"""
            record_to_insert = (cpf, nome, telefone, turno, equipe)
            cursor.execute(sql_insert_query, record_to_insert)
            self.coneccao.commit()
            print("Registro inserido com successo")

        except (Exception, psycopg2.Error) as error:
            if (self.coneccao):
                print("Falha ao inserir registro", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def atualizar_dados(self, cpf, nome, telefone, turno, equipe):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()

            #Antes
            print("Registro Antes da Atualização ")
            sql_select_query = """SELECT * FROM public."Tecnicos" where "CPF" = %s """
            cursor.execute(sql_select_query, (cpf, ))
            registros = cursor.fetchall()
            print(registros)

            #Atualização
            sql_update_query = """Update public."Tecnicos" set "NOME" = %s, "TELEFONE" = %s, "TURNO" = %s, "EQUIPE" = %s where "CPF" = %s"""
            cursor.execute(sql_update_query, (nome, telefone, turno, equipe, cpf))
            self.coneccao.commit()
            print("Registro atualizado com sucesso! ")

            #Depois
            print("Registro Depois da Atualização ")
            cursor.execute(sql_select_query, (cpf, ))
            registros = cursor.fetchone()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def excluir_dados(self, cpf):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_delete_query = """Delete from public."Tecnicos" where "CPF" = %s"""
            cursor.execute(sql_delete_query, (cpf, ))
            self.coneccao.commit()
            print("Registro excluído com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")