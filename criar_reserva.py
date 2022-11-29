from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import tecnicos
import ferramentas
from datetime import datetime, timedelta
import validar_reserva
import reservas
from tkinter import messagebox

class Criar_Reserva_GUI:
    def __init__(self, janela):
        self.banco_tec = tecnicos.Tecnicos_BD()
        self.banco_ferr = ferramentas.Ferramentas_BD()
        self.banco_res = reservas.Reservas_BD()

        janela.geometry('750x550')
        janela.resizable(False, False)
        janela.title('Cadastrar Reserva')
        janela.config(bg='#1e3743')

        # Frame1
        self.frame1 = Frame(janela, bg='#dfe3ee')
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas, bg='#dfe3ee')
        self.aba2 = Frame(self.abas, bg='#dfe3ee')
        self.abas.add(self.aba1, text='Técnicos')
        self.abas.add(self.aba2, text='Ferramentas')
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Aba 1 - Técnicos
        # Linha 1
        Label(self.aba1, text='Procure:', bg='#dfe3ee').place(relx=0, rely=0.01, relwidth=0.08, relheight=0.08)

        self.busca = Entry(self.aba1, bg='#dfe3ee')
        self.busca.place(relx=0.09, rely=0.01, relwidth=0.74, relheight=0.08)

        self.bt_buscar = Button(self.aba1, bg='#dfe3ee', text='Buscar', command= self.buscar1)
        self.bt_buscar.place(relx=0.84, rely=0.01, relwidth=0.07, relheight=0.08)

        self.bt_limpar = Button(self.aba1, bg='#dfe3ee', text='Limpar', command= self.limpar1)
        self.bt_limpar.place(relx=0.92, rely=0.01, relwidth=0.07, relheight=0.08)

        # Linha 2
        self.listaTecnicos = ttk.Treeview(self.aba1, columns=('c1', 'c2', 'c3'), selectmode='browse')
        self.listaTecnicos.heading('#0', text='')
        self.listaTecnicos.heading('c1', text='Nome')
        self.listaTecnicos.heading('c2', text='Nome da Equipe')
        self.listaTecnicos.heading('c3', text='Telefone')
        self.listaTecnicos.column('#0', width=1)
        self.listaTecnicos.column('c1', width=200)
        self.listaTecnicos.column('c2', width=200)
        self.listaTecnicos.column('c3', width=100)
        self.listaTecnicos.place(relx=0.01, rely=0.1, relwidth=0.96, relheight=0.8)

        self.barr_vertical = ttk.Scrollbar(self.aba1, orient='vertical', command=self.listaTecnicos.yview)
        self.listaTecnicos.config(yscrollcommand=self.barr_vertical.set)
        self.barr_vertical.place(relx=0.965, rely=0.1, relwidth=0.03, relheight=0.8)

        # Linha 3
        Label(self.aba1, bg='#dfe3ee', text='Informe Técnico:').place(relx=0, rely=0.9, relwidth=0.16, relheight=0.1)
        self.tec_informado = Entry(self.aba1, bg='#dfe3ee')
        self.tec_informado.place(relx=0.17, rely=0.9, relwidth=0.83, relheight=0.1)

        # Aba2
        # Linha 1
        Label(self.aba2, text='Procure:', bg='#dfe3ee').place(relx=0, rely=0.01, relwidth=0.08, relheight=0.08)

        self.busca2 = Entry(self.aba2, bg='#dfe3ee')
        self.busca2.place(relx=0.09, rely=0.01, relwidth=0.74, relheight=0.08)

        self.bt_buscar2 = Button(self.aba2, bg='#dfe3ee', text='Buscar', command= self.buscar2)
        self.bt_buscar2.place(relx=0.84, rely=0.01, relwidth=0.07, relheight=0.08)

        self.bt_limpar2 = Button(self.aba2, bg='#dfe3ee', text='Limpar', command= self.limpar2)
        self.bt_limpar2.place(relx=0.92, rely=0.01, relwidth=0.07, relheight=0.08)

        # Linha 2 - Ferramentas
        self.listaFerramentas = ttk.Treeview(self.aba2, columns=('c1', 'c2', 'c3'), selectmode='browse')
        self.listaFerramentas.heading('#0', text='')
        self.listaFerramentas.heading('c1', text='Código')
        self.listaFerramentas.heading('c2', text='Nome da Ferramenta')
        self.listaFerramentas.heading('c3', text='Tempo Máximo de Reserva')
        self.listaFerramentas.column('#0', width=1)
        self.listaFerramentas.column('c1', width=50)
        self.listaFerramentas.column('c2', width=450)
        self.listaFerramentas.column('c3', width=50)
        self.listaFerramentas.place(relx=0.01, rely=0.1, relwidth=0.96, relheight=0.8)

        self.barr_vertical2 = ttk.Scrollbar(self.aba2, orient='vertical', command=self.listaFerramentas.yview)
        self.listaFerramentas.config(yscrollcommand=self.barr_vertical2.set)
        self.barr_vertical2.place(relx=0.965, rely=0.1, relwidth=0.03, relheight=0.8)

        # Linha 3
        Label(self.aba2, bg='#dfe3ee', text='Informe Ferramenta:').place(relx=0, rely=0.9, relwidth=0.16, relheight=0.1)
        self.ferr_informada = Entry(self.aba2, bg='#dfe3ee')
        self.ferr_informada.place(relx=0.17, rely=0.9, relwidth=0.83, relheight=0.1)

        # Frame 2
        self.frame2 = Frame(janela, bg='#dfe3ee')
        self.frame2.place(relx=0.02, rely=0.54, relwidth=0.96, relheight=0.34)
        # Linha 1
        Label(self.frame2, text='Informe data de retirada', font=('bold'), bg='#dfe3ee').place(relx=0.02, rely=0.02,
                                                                                          relwidth=0.3, relheight=0.1)

        self.data_retirada = DateEntry(self.frame2, locale='pt_br')
        self.data_retirada.place(relx=0.355, rely=0.02, relwidth=0.13, relheight=0.13)

        Label(self.frame2, text='Hora de retirada', font=('bold'), bg='#dfe3ee').place(relx=0.5, rely=0.02, relwidth=0.21,
                                                                                  relheight=0.1)

        self.hora_retirada = ttk.Combobox(self.frame2, textvariable=StringVar())
        h = []
        for i in range(24):
            h.append(i)
        self.hora_retirada['values'] = h
        self.hora_retirada.place(relx=0.745, rely=0.02, relwidth=0.08, relheight=0.13)

        self.minuto_retirada = ttk.Combobox(self.frame2, textvariable=StringVar())
        m = []
        for i in range(60):
            m.append(i)
        self.minuto_retirada['values'] = m
        self.minuto_retirada.place(relx=0.835, rely=0.02, relwidth=0.08, relheight=0.13)

        # Linha 2
        Label(self.frame2, text='Informe data de devolução', font=('bold'), bg='#dfe3ee').place(relx=0.02, rely=0.5,
                                                                                           relwidth=0.325,
                                                                                           relheight=0.1)

        self.data_devolucao = DateEntry(self.frame2, locale='pt_br')
        self.data_devolucao.place(relx=0.355, rely=0.5, relwidth=0.13, relheight=0.13)

        Label(self.frame2, text='Hora de Devolução', font=('bold'), bg='#dfe3ee').place(relx=0.5, rely=0.5, relwidth=0.235,
                                                                                   relheight=0.1)

        self.hora_de_devolucao = ttk.Combobox(self.frame2, textvariable=StringVar())
        h2 = []
        for i in range(24):
            h2.append(i)
        self.hora_de_devolucao['values'] = h2
        self.hora_de_devolucao.place(relx=0.745, rely=0.5, relwidth=0.08, relheight=0.13)

        self.minuto_devolucao = ttk.Combobox(self.frame2, textvariable=StringVar())
        m2 = []
        for i in range(60):
            m2.append(i)
        self.minuto_devolucao['values'] = m2
        self.minuto_devolucao.place(relx=0.835, rely=0.5, relwidth=0.08, relheight=0.13)

        # Resto da Janela
        self.bt_reserva = Button(janela, text='Confirmar\nReserva', font=('verdana', 11, 'bold'), bg='#dfe3ee', command= self.autorizar_reserva)
        self.bt_reserva.place(relx=0.02, rely=0.9, relwidth=0.15, relheight=0.08)

        self.bt_cancelar = Button(janela, text='Cancelar', font=('verdana', 11, 'bold'), bg='#dfe3ee',
                             command=janela.destroy)
        self.bt_cancelar.place(relx=0.83, rely=0.9, relwidth=0.15, relheight=0.08)

        # Dados da janela
        self.carregar_dados_iniciais()

        # Funções da janela
        self.listaTecnicos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados1)
        self.listaFerramentas.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados2)

    def carregar_dados_iniciais(self):
        try:
            # TECNICOS
            registro = self.banco_tec.selecionar_dados()
            registro_aux = []
            for item in registro:
                registro_aux.append((item[1], item[4], item[2]))
            for item in registro_aux:
                self.listaTecnicos.insert('', 'end', values=item)
            print('Dados dos técnicos impressos')
            # FERRAMENTAS
            registro2 = self.banco_ferr.selecionar_dados()
            registro2_aux = []
            for item in registro2:
                registro2_aux.append((item[0], item[1], item[9]))
            for item in registro2_aux:
                self.listaFerramentas.insert('', 'end', values=item)
            print('Dados das ferramentas impressos')
        except:
            print('Ainda existem dados para carregar')

    def buscar1(self):
        try:
            self.listaTecnicos.delete(*self.listaTecnicos.get_children())
            busca = self.busca.get()
            registro = self.banco_tec.selecionar_dados_especificos('NOME', busca)
            registro_aux = []
            for item in registro:
                registro_aux.append((item[1], item[4], item[2]))
            for item in registro_aux:
                self.listaTecnicos.insert('', 'end', values=item)
        except:
            print('Não foi possível buscar os técnicos')

    def buscar2(self):
        try:
            self.listaFerramentas.delete(*self.listaFerramentas.get_children())
            busca = self.busca2.get()
            registro2 = self.banco_ferr.selecionar_dados_especificos('DESCRICAO', busca)
            registro2_aux = []
            for item in registro2:
                registro2_aux.append((item[0], item[1], item[9]))
            for item in registro2_aux:
                self.listaFerramentas.insert('', 'end', values=item)
        except:
            print('Não foi possível buscar a ferramenta')

    def limpar1(self):
        try:
            self.busca.delete(0, END)
            print('Barra Limpa')
        except:
            print('Não foi possível limpar')

    def limpar2(self):
        try:
            self.busca2.delete(0, END)
            print('Barra Limpa')
        except:
            print('Não foi possível limpar')

    def apresentarRegistrosSelecionados1(self, event):
        self.limpar1()
        for selection in self.listaTecnicos.selection():
            item = self.listaTecnicos.item(selection)
            nome = item["values"][0]
            self.tec_informado.insert(0, nome)

    def apresentarRegistrosSelecionados2(self, event):
        self.limpar2()
        for selection in self.listaFerramentas.selection():
            item = self.listaFerramentas.item(selection)
            descricao = item["values"][1]
            self.ferr_informada.insert(0, descricao)

    def autorizar_reserva(self):
        try:
            nome = self.tec_informado.get()
            descricao = self.ferr_informada.get()
            data_retirada = self.data_retirada.get()
            hora_retirada = self.hora_retirada.get()
            minuto_retirada = self.minuto_retirada.get()
            data_devolucao = self.data_devolucao.get()
            hora_devolucao = self.hora_de_devolucao.get()
            minuto_devolucao = self.minuto_devolucao.get()
            if nome and descricao and data_retirada and hora_retirada and minuto_retirada and data_devolucao and hora_devolucao and minuto_devolucao !='':
                retirada_str = data_retirada + ' ' + hora_retirada + ':' + minuto_retirada
                retirada = datetime.strptime(retirada_str, '%d/%m/%Y %H:%M')
                devolucao_str = data_devolucao + ' ' + hora_devolucao + ':' + minuto_devolucao
                devolucao = datetime.strptime(devolucao_str, '%d/%m/%Y %H:%M')
                print(retirada, devolucao)
                registro = self.banco_ferr.selecionar_dados_especificos('DESCRICAO', descricao)
                for item in registro:
                    codigo = item[0]
                    tempo = item[9]
                tempo = timedelta(hours= tempo)
                if validar_reserva.testes(retirada, devolucao, tempo):
                    registro_reserva = self.banco_res.selecionar_dados_especificos('DESCRICAO', descricao)
                    if registro_reserva != []:
                        auxiliar1 = []
                        for item in registro_reserva:

                            if retirada < datetime.strptime(item[4], '%Y-%m-%d %H:%M:%S'):
                                auxiliar1.append(item)
                        if auxiliar1 != []:
                            auxiliar2 = []
                            for item in auxiliar1:
                                if devolucao > datetime.strptime(item[3], '%Y-%m-%d %H:%M:%S'):
                                    auxiliar2.append(item)
                            if auxiliar2 != []:
                                texto = 'Esta ferramenta não está disponível para este período'
                                messagebox.showinfo('Alerta!!!', texto)
                            else:
                                self.inserir_reserva(codigo, descricao, nome, retirada, devolucao)
                        else:
                            self.inserir_reserva(codigo, descricao, nome, retirada, devolucao)
                    else:
                        self.inserir_reserva(codigo, descricao, nome, retirada, devolucao)
                else:
                    texto = 'Esta ferramenta não está disponível para este período'
                    messagebox.showinfo('Alerta!!!', texto)
            else:
                texto = 'Existem campos não preenchidos'
                messagebox.showinfo('Alerta!!!', texto)
        except:
            print('Não foi possível concluir a reseerva')

    def inserir_reserva(self, codigo, descricao, nome, retirada, devolucao):
        try:
            registro = self.banco_tec.selecionar_dados_especificos('NOME', nome)
            for item in registro:
                telefone = item[2]
                equipe = item[4]
            data_retirada = str(retirada)
            data_devolucao = str(devolucao)
            self.banco_res.inserir_dados(codigo, descricao, nome, data_retirada, data_devolucao, equipe, telefone)
        except:
            print('Não foi possível registrar a reserva ')