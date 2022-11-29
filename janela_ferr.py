from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ferramentas as ferr
import cadastro_ferramentas
import atualizar_ferramentas

class Ferraments_GUI:
    def __init__(self, janela):
        self.banco_ferr = ferr.Ferramentas_BD()
        ### Construção da janela
        janela.geometry('900x500')
        janela.resizable(False, False)
        janela.title('Lista de Ferramentas')

        # Linha 1
        self.cabecalho = Label(janela, text='Pesquisar ferramenta por nome ou fabricante:' ).place(relx=0, rely=0, relwidth=0.3, relheight=0.1)

        # linha 2
        self.txt_pesquisa = Entry(janela)
        self.txt_pesquisa.place(relx=0.015, rely=0.1, relwidth=0.55, relheight=0.06)

        self.cb_escolha = ttk.Combobox(janela, textvariable=StringVar())
        self.cb_escolha['values'] = ('Nome', 'Fabricante')
        self.cb_escolha.place(relx=0.570, rely=0.1, relwidth=0.2, relheight=0.06)

        self.bt_pesquisa = Button(janela, text='Procurar', command = self.buscar)
        self.bt_pesquisa.place(relx=0.775, rely=0.1, relwidth=0.1, relheight=0.06)

        self.bt_limpar = Button(janela, text='Limpar', command = self.limpar)
        self.bt_limpar.place(relx=0.880, rely=0.1, relwidth=0.1, relheight=0.06)

        # Linha 3
        self.listaFerr = ttk.Treeview(janela, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'), selectmode='browse')
        self.listaFerr.heading('#0', text='')
        self.listaFerr.heading('c1', text='Código')
        self.listaFerr.heading('c2', text='Nome')
        self.listaFerr.heading('c3', text='Fabricante')
        self.listaFerr.heading('c4', text='Voltagem')
        self.listaFerr.heading('c5', text='Part Number')
        self.listaFerr.heading('c6', text='Tamanho')
        self.listaFerr.heading('c7', text='Unidade de Medida')
        self.listaFerr.heading('c8', text='Tipo de Ferramenta')
        self.listaFerr.heading('c9', text='Material da Ferramenta')
        self.listaFerr.heading('c10', text='Tempo máximo de reserva')
        self.listaFerr.column('#0', width=1)
        self.listaFerr.column('c1', width=80)
        self.listaFerr.column('c2', width=250)
        self.listaFerr.column('c3', width=80)
        self.listaFerr.column('c4', width=80)
        self.listaFerr.column('c5', width=100)
        self.listaFerr.column('c6', width=120)
        self.listaFerr.column('c7', width=120)
        self.listaFerr.column('c8', width=120)
        self.listaFerr.column('c9', width=120)
        self.listaFerr.column('c10', width=150)
        self.listaFerr.place(relx=0.015, rely=0.2, relwidth=0.95, relheight=0.6)

        self.barr_vert = ttk.Scrollbar(janela, orient='vertical', command= self.listaFerr.yview)
        self.listaFerr.config(yscrollcommand=self.barr_vert.set)
        self.barr_vert.place(relx=0.965, rely=0.2, relwidth=0.02, relheight=0.6)

        self.barr_hor = ttk.Scrollbar(janela, orient='horizontal', command = self.listaFerr.xview)
        self.listaFerr.config(xscrollcommand=self.barr_hor.set)
        self.barr_hor.place(relx=0.015, rely=0.81, relwidth=0.95, relheight=0.03)

        # Linha 4
        self.bt_novo = Button(janela, text='Novo', command= self.tela_de_cadastro)
        self.bt_novo.place(relx=0.015, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_alterar = Button(janela, text='Alterar', command = self.tela_de_alteracao)
        self.bt_alterar.place(relx=0.145, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_excluir = Button(janela, text='Excluir', command= self.excluir)
        self.bt_excluir.place(relx=0.275, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_atualizar = Button(janela, text='Atualizar', command= self.atualizar)
        self.bt_atualizar.place(relx=0.405, rely=0.9, relwidth=0.1, relheight=0.06)

        self.bt_fechar = Button(janela, text='Fechar', command=janela.destroy)
        self.bt_fechar.place(relx=0.88, rely=0.9, relwidth=0.1, relheight=0.06)

        # Dados da janela
        self.carregarDadosIniciais()

    def carregarDadosIniciais(self):
        try:
            registros = self.banco_ferr.selecionar_dados()
            print("************ dados dsponíveis no BD ***********")
            for item in registros:
                self.listaFerr.insert('', 'end', values = item)
            print('Dados do banco impressos')
        except:
            print('Ainda não existem dados para carregar')

    def buscar(self):
        try:
            self.listaFerr.delete(*self.listaFerr.get_children())
            escolha = self.cb_escolha.get()
            if escolha == 'Nome':
                busca = self.txt_pesquisa.get()
                registro = self.banco_ferr.selecionar_dados_especificos('DESCRICAO', busca)
            elif escolha == 'Fabricante':
                busca = self.txt_pesquisa.get()
                registro = self.banco_ferr.selecionar_dados_especificos('FABRICANTE', busca)
            else:
                texto = 'Precisa selecionar o tipo de pesquisa'
                messagebox.showinfo('Alerta!!!', texto)
            for item in registro:
                self.listaFerr.insert('', 'end', values=item)
        except:
            print('Não foi possível buscar a ferramenta')

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
            self.cad_int = cadastro_ferramentas.Ferr_Cadastro_GII(self.janCad)
        except:
            print('Não foi possível iniciar cadastro')

    def atualizar(self):
        self.listaFerr.delete(*self.listaFerr.get_children())
        self.carregarDadosIniciais()

    def dados_selecionados(self):
        try:
            for selection in self.listaFerr.selection():
                item = self.listaFerr.item(selection)
            lista = item["values"][0:10]
            print(lista)
            return lista
        except:
            print('Nenhuma ferramenta selecionada')
            texto = 'Nenhuma ferramenta selecionada'
            messagebox.showinfo('Alerta!!!', texto)

    def tela_de_alteracao(self):
        try:
            lista = self.dados_selecionados()
            codigo, descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res = lista
            self.janAlt = Toplevel()
            #self.janAlt.transient(janela)
            self.janAlt.focus_force()
            self.janAlt.grab_set()
            self.alt_int = atualizar_ferramentas.Ferr_Ateracao_GUI(self.janAlt, codigo, descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res)
        except:
            print('Não foi possível iniciar a alteração')

    def excluir(self):
        try:
            lista = self.dados_selecionados()
            codigo = lista[0]
            if messagebox.askyesno('Verificar', 'Tem certeza que quer excluir esta ferramenta'):
                self.banco_ferr.excluir_dados(codigo)
                messagebox.showwarning('Yes', 'A ferramenta foi excluída')
                self.atualizar()
        except:
            print('Não foi possível excluir a ferramenta')