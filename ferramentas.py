import psycopg2

class Ferramentas_BD:
    def __init__(self):
        pass

    def abrir_coneccao(self):
        try:
            self.coneccao = psycopg2.connect(user = 'postgres', password = 'INSIRA-SUA-SENHA', host = '127.0.0.1', port = '5432', database = 'postgres')
            print('Conexão aberta')
        except (Exception, psycopg2.Error) as error:
            if (self.coneccao):
                print('Falha ao se conectar a banco de dados', error)

    def selecionar_dados(self):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_select_query = """select * from public."FERRAMENTAS" order by "CODIGO" ASC"""
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
            sql_select_query2 = f"""SELECT * FROM public."FERRAMENTAS" WHERE "{tipo_de_busca}" LIKE '%{busca}%' """
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

    def gerar_codigo(self):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_select_query = """SELECT "CODIGO" FROM public."FERRAMENTAS" ORDER BY "CODIGO" ASC """
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            codigo = 10001
            for x in registros:
                if codigo in x:
                    codigo = codigo + 1
            print(codigo)
            return codigo

        except (Exception, psycopg2.Error) as error:
            print('Falha ao gerar código', error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print('Conexão com o banco de dados fechada')

    def inserir_dados(self, descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res):
        try:
            codigo = self.gerar_codigo()
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_insert_query = """ INSERT INTO public."FERRAMENTAS"("CODIGO", "DESCRICAO", "FABRICANTE", "VOLTAGEM", "PART_NUMBER", "TAMANHO", "UNIDADE_DE_MEDIDA", "TIPO_DE_FERRAMENTA", "MATERIAL_DA_FERRAMENTA", "TEMPO_MAXIMO_DA_RESERVA") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record_to_insert = (codigo, descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res)
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

    def atualizar_dados(self, codigo, descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()

            #Antes
            print("Registro Antes da Atualização ")
            sql_select_query = """SELECT * FROM public."FERRAMENTAS" where "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo, ))
            registros = cursor.fetchall()
            print(registros)

            #Atualização
            sql_update_query = """Update public."FERRAMENTAS" set "DESCRICAO" = %s, "FABRICANTE" = %s, "VOLTAGEM" = %s, "PART_NUMBER" = %s, "TAMANHO" = %s, "UNIDADE_DE_MEDIDA" = %s, "TIPO_DE_FERRAMENTA" = %s, "MATERIAL_DA_FERRAMENTA" = %s, "TEMPO_MAXIMO_DA_RESERVA" = %s where "CODIGO" = %s"""
            cursor.execute(sql_update_query, (descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res, codigo))
            self.coneccao.commit()
            print("Registro atualizado com sucesso!")

            #Depois
            print("Registro Depois da Atualização ")
            cursor.execute(sql_select_query, (codigo, ))
            registros = cursor.fetchone()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def excluir_dados(self, codigo):
        try:
            self.abrir_coneccao()
            cursor = self.coneccao.cursor()
            sql_delete_query = """Delete from public."FERRAMENTAS" where "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo, ))
            self.coneccao.commit()
            print("Registro excluído com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)

        finally:
            if (self.coneccao):
                cursor.close()
                self.coneccao.close()
                print("A conexão com o PostgreSQL foi fechada.")