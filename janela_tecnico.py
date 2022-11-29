from tkinter import *
from tkinter import ttk
import tecnicos
from tkinter import messagebox
import cadastro_tecnicos
import atualizacao_tecnicos

class Tecnicos_GUI:
    def __init__(self, janela):
        self.banco_tecnicos = tecnicos.Tecnicos_BD()
        ### Construção da janela
        janela.geometry('900x500')
        janela.resizable(False, False)
        janela.title('Lista de Técnicos')

        # Linha 1
        Label(janela, text='Pesquisar técnico por Nome ou CPF:', ).place(relx=0.015, rely=0, relwidth=0.212, relheight=0.1)

        # linha 2
        self.txt_pesquisa = Entry(janela)
        self.txt_pesquisa.place(relx=0.015, rely=0.1, relwidth=0.55, relheight=0.06)

        self.cb_escolha = ttk.Combobox(janela, textvariable=StringVar())
        self.cb_escolha['values'] = ('Nome', 'CPF')
        self.cb_escolha.place(relx=0.570, rely=0.1, relwidth=0.2, relheight=0.06)

        self.bt_pesquisa = Button(janela, text='Procurar', command= self.buscar)
        self.bt_pesquisa.place(relx=0.775, rely=0.1, relwidth=0.1, relheight=0.06)

        self.bt_limpar = Button(janela, text='Limpar', command= self.limpar)
        self.bt_limpar.place(relx=0.880, rely=0.1, relwidth=0.1, relheight=0.06)

        # Linha 3
        self.listaTecnicos = ttk.Treeview(janela, columns=('c1', 'c2', 'c3', 'c4', 'c5'), selectmode='browse')
        self.listaTecnicos.heading('#0', text='')
        self.listaTecnicos.heading('c1', text='CPF')
        self.listaTecnicos.heading('c2', text='Nome')
        self.listaTecnicos.heading('c3', text='Telefone')
        self.listaTecnicos.heading('c4', text='Turno')
        self.listaTecnicos.heading('c5', text='Nome da Equipe')
        self.listaTecnicos.column('#0', width=1)
        self.listaTecnicos.column('c1', width=50)
        self.listaTecnicos.column('c2', width=200)
        self.listaTecnicos.column('c3', width=50)
        self.listaTecnicos.column('c4', width=50)
        self.listaTecnicos.column('c5', width=150)
        self.listaTecnicos.place(relx=0.015, rely=0.2, relwidth=0.95, relheight=0.6)

        self.barr_vert = ttk.Scrollbar(janela, orient='vertical', command= self.listaTecnicos.yview)
        self.listaTecnicos.config(yscrollcommand= self.barr_vert.set)
        self.barr_vert.place(relx=0.965, rely=0.2, relwidth=0.02, relheight=0.6)

        #self.barr_hor = ttk.Scrollbar(janela, orient='horizontal', command= self.listaTecnicos.xview)
        #self.listaTecnicos.config(xscrollcommand= self.barr_hor.set)
        #self.barr_hor.place(relx=0.015, rely=0.81, relwidth=0.95, relheight=0.03)

        # Linha 4
        self.bt_novo = Button(janela, text='Novo', command= self.tela_de_cadastro)
        self.bt_novo.place(relx=0.015, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_alterar = Button(janela, text='Alterar', command= self.tela_de_alteracao)
        self.bt_alterar.place(relx=0.145, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_excluir = Button(janela, text='Excluir', command= self.excluir)
        self.bt_excluir.place(relx=0.275, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_atualizar = Button(janela, text='Atualizar', command= self.atualizar)
        self.bt_atualizar.place(relx=0.405, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_fechar = Button(janela, text='Fechar', command=janela.destroy)
        self.bt_fechar.place(relx=0.88, rely=0.9, relwidth=0.1, relheight=0.06)

        #Dados da janela
        self.carregarDadosIniciais()

    def carregarDadosIniciais(self):
        try:
            registros = self.banco_tecnicos.selecionar_dados()
            print("************ dados dsponíveis no BD ***********")
            for item in registros:
                self.listaTecnicos.insert('', 'end', values = item)
            print('Dados do banco impressos')
        except:
            print('Ainda não existem dados para carregar')

    def buscar(self):
        try:
            self.listaTecnicos.delete(*self.listaTecnicos.get_children())
            escolha = self.cb_escolha.get()
            if escolha == 'Nome':
                busca = self.txt_pesquisa.get()
                registro = self.banco_tecnicos.selecionar_dados_especificos('NOME', busca)
            elif escolha == 'CPF':
                busca = self.txt_pesquisa.get()
                registro = self.banco_tecnicos.selecionar_dados_especificos('CPF', busca)
            else:
                texto = 'Precisa selecionar o tipo de pesquisa'
                messagebox.showinfo('Alerta!!!', texto)
            for item in registro:
                self.listaTecnicos.insert('', 'end', values=item)
        except:
            print('Não foi possível buscar os técnicos')

    def limpar(self):
        try:
            self.txt_pesquisa.delete(0, END)
            print('Barra Limpa')
        except:
            print('Não foi possível limpar')

    def tela_de_cadastro(self):
        try:
            self.janCad = Toplevel()
            #self.janCad.transient(janela)
            self.janCad.focus_force()
            self.janCad.grab_set()
            self.cad_int = cadastro_tecnicos.Tecnico_Cadastro_GUI(self.janCad)
        except:
            print('Não foi possível iniciar cadastro')

    def atualizar(self):
        self.listaTecnicos.delete(*self.listaTecnicos.get_children())
        self.carregarDadosIniciais()

    def dados_selecionados(self):
        try:
            for selection in self.listaTecnicos.selection():
                item = self.listaTecnicos.item(selection)
            lista = item["values"][0:5]
            print(lista)
            return lista
        except:
            print('Nenhum Técnico selecionado')
            texto = 'Nenhum Técnico selecionado'
            messagebox.showinfo('Alerta!!!', texto)

    def tela_de_alteracao(self):
        try:
            lista = self.dados_selecionados()
            cpf, nome, telefone, turno, equipe = lista
            self.janAlt = Toplevel()
            #self.janAlt.transient(janela)
            self.janAlt.focus_force()
            self.janAlt.grab_set()
            self.alt_int = atualizacao_tecnicos.Tecnico_Alteracao_GUI(self.janAlt, cpf, nome, telefone, turno, equipe)
        except:
            print('Não foi possível iniciar a alteração')

    def excluir(self):
        try:
            lista = self.dados_selecionados()
            cpf = lista[0]
            if messagebox.askyesno('Verificar', 'Tem certeza que quer remover este técnico'):
                self.banco_tecnicos.excluir_dados(cpf)
                messagebox.showwarning('Yes', 'O técnico foi removido')
                self.atualizar()
        except:
            print('Não foi possível excluir a ferramenta')