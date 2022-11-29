from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import reservas
import criar_reserva
from datetime import datetime
import pandas

class Reservas_GUI:
    def __init__(self, janela):
        self.banco_res = reservas.Reservas_BD()
        ### Construção da janela
        janela.geometry('900x500')
        janela.resizable(False, False)
        janela.title('Lista de Técnicos')

        # Linha 1
        Label(janela, text='Pesquisar reserva por técnico ou ferramenta:', ).place(relx=0.015, rely=0, relwidth=0.26, relheight=0.1)

        # linha 2
        self.txt_pesquisa = Entry(janela)
        self.txt_pesquisa.place(relx=0.015, rely=0.1, relwidth=0.55, relheight=0.06)

        self.cb_escolha = ttk.Combobox(janela, textvariable=StringVar())
        self.cb_escolha['values'] = ('Técnico', 'Ferramenta')
        self.cb_escolha.place(relx=0.570, rely=0.1, relwidth=0.2, relheight=0.06)

        self.bt_pesquisa = Button(janela, text='Procurar', command= self.buscar)
        self.bt_pesquisa.place(relx=0.775, rely=0.1, relwidth=0.1, relheight=0.06)

        self.bt_limpar = Button(janela, text='Limpar', command= self.limpar)
        self.bt_limpar.place(relx=0.880, rely=0.1, relwidth=0.1, relheight=0.06)

        # Linha 3
        self.listaReservas = ttk.Treeview(janela, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'), selectmode='browse')
        self.listaReservas.heading('#0', text='')
        self.listaReservas.heading('c1', text='Codigo')
        self.listaReservas.heading('c2', text='Ferramenta')
        self.listaReservas.heading('c3', text='Técnico')
        self.listaReservas.heading('c4', text='Data de Retirada')
        self.listaReservas.heading('c5', text='Data de Devolução')
        self.listaReservas.heading('c6', text='Equipe')
        self.listaReservas.heading('c7', text='Telefone')
        self.listaReservas.column('#0', width=1)
        self.listaReservas.column('c1', width=50)
        self.listaReservas.column('c2', width=250)
        self.listaReservas.column('c3', width=150)
        self.listaReservas.column('c4', width=110)
        self.listaReservas.column('c5', width=110)
        self.listaReservas.column('c6', width=140)
        self.listaReservas.column('c7', width=110)
        self.listaReservas.place(relx=0.015, rely=0.2, relwidth=0.95, relheight=0.6)

        self.barr_vert = ttk.Scrollbar(janela, orient='vertical', command= self.listaReservas.yview)
        self.listaReservas.config(yscrollcommand= self.barr_vert.set)
        self.barr_vert.place(relx=0.965, rely=0.2, relwidth=0.02, relheight=0.6)

        self.barr_hor = ttk.Scrollbar(janela, orient='horizontal', command= self.listaReservas.xview)
        self.listaReservas.config(xscrollcommand= self.barr_hor.set)
        self.barr_hor.place(relx=0.015, rely=0.81, relwidth=0.95, relheight=0.03)

        # Linha 4
        self.bt_reserva = Button(janela, text='Reservar', command= self.tela_para_reservar)
        self.bt_reserva.place(relx=0.015, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_excluir = Button(janela, text='Excluir', command= self.excluir)
        self.bt_excluir.place(relx=0.145, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_atualizar = Button(janela, text='Atualizar', command=self.atualizar)
        self.bt_atualizar.place(relx=0.275, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_exportar = Button(janela, text = 'Exportar', command= self.exportar)
        self.bt_exportar.place(relx = 0.405, rely = 0.9, relwidth= 0.1, relheight= 0.06)

        self.bt_fechar = Button(janela, text='Fechar', command=janela.destroy)
        self.bt_fechar.place(relx=0.88, rely=0.9, relwidth=0.1, relheight=0.06)

        #Dados da janela
        self.carregarDadosIniciais()

    def carregarDadosIniciais(self):
        try:
            registros = self.banco_res.selecionar_dados()
            print("************ dados dsponíveis no BD ***********")
            for item in registros:
                self.listaReservas.insert('', 'end', values = item)
            print('Dados do banco impressos')
        except:
            print('Ainda não existem dados para carregar')

    def buscar(self):
        try:
            self.listaReservas.delete(*self.listaReservas.get_children())
            escolha = self.cb_escolha.get()
            if escolha == 'Técnico':
                busca = self.txt_pesquisa.get()
                registro = self.banco_res.selecionar_dados_especificos('NOME', busca)
            elif escolha == 'Ferramenta':
                busca = self.txt_pesquisa.get()
                registro = self.banco_res.selecionar_dados_especificos('DESCRICAO', busca)
            else:
                texto = 'Precisa selecionar o tipo de pesquisa'
                messagebox.showinfo('Alerta!!!', texto)
            for item in registro:
                self.listaReservas.insert('', 'end', values=item)
        except:
            print('Não foi possível buscar as reservas')

    def limpar(self):
        try:
            self.txt_pesquisa.delete(0, END)
            print('Barra Limpa')
        except:
            print('Não foi possível limpar')

    def atualizar(self):
        self.listaReservas.delete(*self.listaReservas.get_children())
        self.carregarDadosIniciais()
    
    def dados_selecionados(self):
        try:
            for selection in self.listaReservas.selection():
                item = self.listaReservas.item(selection)
            lista = item["values"][0:5]
            print(lista)
            return lista
        except:
            print('Nenhuma reserva selecionada')
            texto = 'Nenhuma reserva selecionada'
            messagebox.showinfo('Alerta!!!', texto)

    def tela_para_reservar(self):
        try:
            self.janRes = Toplevel()
            #self.janRes.transient(janela)
            self.janRes.focus_force()
            self.janRes.grab_set()
            self.fazerRes_int = criar_reserva.Criar_Reserva_GUI(self.janRes)
        except:
            print('Não foi possível iniciar cadastro')

    def excluir(self):
        try:
            lista = self.dados_selecionados()
            codigo = lista[0]
            data_retirada_str = lista[3]
            data_deevolucao_str = lista[4]
            data_retirada = datetime.strptime(data_retirada_str, '%Y-%m-%d %H:%M:%S')
            data_deevolucao = datetime.strptime(data_deevolucao_str, '%Y-%m-%d %H:%M:%S')
            data_hoje = datetime.now()
            if data_retirada > data_hoje:
                if messagebox.askyesno('Verificar', 'Tem certeza que quer cancelar esta reserva'):
                    self.banco_res.excluir_dados(codigo, data_retirada_str)
                    messagebox.showwarning('Yes', 'A reserva foi cancelada')
                    self.atualizar()
            else:
                if data_hoje > data_deevolucao:
                    if messagebox.askyesno('Verificar', 'Tem certeza que quer cancelar esta reserva'):
                        self.banco_res.excluir_dados(codigo, data_retirada_str)
                        messagebox.showwarning('Yes', 'A reserva foi cancelada')
                        self.atualizar()
                else:
                    texto = 'Não é possível excluir a reserva antes da devolução'
                    messagebox.showinfo('Alerta!!!', texto)
        except:
            print('Não foi possível excluir a ferramenta')

    def exportar(self):
        try:
            registro = self.banco_res.selecionar_dados()
            dicionario = {'Código': [], 'Descrição': [], 'Técnico': [], 'Data Retirada': [], 'Data Devolução': [],
                          'Equipe': [], 'Telefone': []}
            for item in registro:
                dicionario['Código'].append(item[0])
                dicionario['Descrição'].append(item[1])
                dicionario['Técnico'].append(item[2])
                dicionario['Data Retirada'].append(item[3])
                dicionario['Data Devolução'].append(item[4])
                dicionario['Equipe'].append(item[5])
                dicionario['Telefone'].append(item[6])
            df_registro = pandas.DataFrame(dicionario)
            df_registro.to_excel('Lista de Reservas.xlsx', index=False)
            texto = 'Arquivo excel criado'
            messagebox.showinfo('Alerta!!!', texto)
        except:
            print('Não foi possível gerar o arquivo')