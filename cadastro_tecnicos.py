from tkinter import *
import tecnicos
import verificacao_cpf
from tkinter import ttk
from tkinter import messagebox

class Tecnico_Cadastro_GUI:
    def __init__(self, janela):
        self.banco_tecnicos = tecnicos.Tecnicos_BD()
        print('Método construtor chamado')
        def limitar_entrada(n):
            if len(n) > 11:
                return False
            return True
        restringir = janela.register(func= limitar_entrada)

        ### Construção da Janela
        janela.geometry('500x300')
        janela.resizable(False, False)
        janela.title('Cadastro de Técnicos')

        # Linha 1
        Label(janela, text='Nome Completo:', font=("Times New Roman", 15)).place(relx=0, rely=0, relwidth=0.3, relheight=0.1)

        # Linha 2
        self.nome = Entry(janela, font=("Times New Roman", 15))
        self.nome.place(relx=0.01, rely=0.12, relwidth=0.97, relheight=0.1)

        # Linha 3
        Label(janela, text='CPF:', font=("Times New Roman", 15)).place(relx=0, rely=0.24, relwidth=0.1, relheight=0.1)

        self.cpf = Entry(janela, font=("Times New Roman", 15), validate= 'key', validatecommand= (restringir, '%P'))
        self.cpf.place(relx=0.11, rely=0.24, relwidth=0.3, relheight=0.1)

        Label(janela, text='Telefone:', font=("Times New Roman", 15)).place(relx=0.40, rely=0.24, relwidth=0.3, relheight=0.1)

        self.ddd = Entry(janela, font=("Times New Roman", 15))
        self.ddd.place(relx=0.66, rely=0.24, relwidth=0.07, relheight=0.1)

        self.numero = Entry(janela, font=("Times New Roman", 15))
        self.numero.place(relx=0.75, rely=0.24, relwidth=0.23, relheight=0.1)

        # Linha 4
        Label(janela, text='Nome da Equipe:', font=("Times New Roman", 15)).place(relx=0, rely=0.36, relwidth=0.3,
                                                                          relheight=0.1)
        # Linha 5
        self.equipe = Entry(janela, font=("Times New Roman", 15))
        self.equipe.place(relx=0.01, rely=0.48, relwidth=0.97, relheight=0.1)

        # Linha 6
        Label(janela, text='Turno:', font=("Times New Roman", 15)).place(relx=0, rely=0.6, relwidth=0.1, relheight=0.1)
        self.escolha = ttk.Combobox(janela, textvariable=StringVar())
        self.escolha['values'] = ('Manhã', 'Tarde', 'Noite')
        self.escolha.place(relx=0.12, rely=0.6, relwidth=0.3, relheight=0.1)

        # Linha 7
        self.bt_cadastrar = Button(janela, text='Cadastrar', font=("Times New Roman", 15), command= self.cadastrar)
        self.bt_cadastrar.place(relx=0.05, rely=0.78, relwidth=0.25, relheight=0.1)

        self.bt_limpar = Button(janela, text='Limpar', font=("Times New Roman", 15), command= self.limpar)
        self.bt_limpar.place(relx=0.375, rely=0.78, relwidth=0.25, relheight=0.1)

        self.bt_cancelar = Button(janela, text='Cancelar', font=("Times New Roman", 15), command=janela.destroy)
        self.bt_cancelar.place(relx=0.7, rely=0.78, relwidth=0.25, relheight=0.1)

    def cadastrar(self):
        try:
            nome = self.nome.get()
            cpf = self.cpf.get()
            ddd = self.ddd.get()
            numero = self.numero.get()
            equipe = self.equipe.get()
            escolha = self.escolha.get()
            if nome and cpf and ddd and numero and equipe and escolha != '':
                if verificacao_cpf.validacao_de_cpf(cpf):
                    cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
                    if len(numero) == 8 and numero[0] == '3':
                        telefone = ddd + ' ' + numero[0:4] + '-' + numero[4:8]
                        self.banco_tecnicos.inserir_dados(cpf, nome, telefone, escolha, equipe)
                    elif len(numero) == 9 and numero[0] == '9':
                        telefone = ddd + ' ' + numero[0:5] + '-' + numero[5:9]
                        self.banco_tecnicos.inserir_dados(cpf, nome, telefone, escolha, equipe)
                    else:
                        texto = 'Número informado inválido'
                        messagebox.showinfo('Alerta!!!', texto)
                else:
                    texto = 'CPF inválido'
                    messagebox.showinfo('Alerta!!!', texto)
            else:
                texto = 'Existem campos não preenchidos'
                messagebox.showinfo('Alerta!!!', texto)
        except:
            print('Não foi possível concluir o cadastro')

    def limpar(self):
        try:
            self.nome.delete(0, END)
            self.cpf.delete(0, END)
            self.ddd.delete(0, END)
            self.numero.delete(0, END)
            self.equipe.delete(0, END)
            self.escolha.delete(0, END)
            print('Campos limpos')
        except:
            print('Não foi possível limpar os campos')