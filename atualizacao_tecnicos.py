from tkinter import *
import tecnicos
from tkinter import ttk
from tkinter import messagebox

class Tecnico_Alteracao_GUI:
    def __init__(self, janela, cpf, nome, telefone, turno, equipe):
        self.banco_tecnicos = tecnicos.Tecnicos_BD()
        ddd = telefone[0:2]
        numero = telefone[3:len(telefone)]
        print('Método construtor chamado')

        ### Construção da Janela
        janela.geometry('500x300')
        janela.resizable(False, False)
        janela.title('Cadastro de Técnicos')

        # Linha 1
        Label(janela, text='Nome Completo:', font=("Times New Roman", 15)).place(relx=0, rely=0, relwidth=0.3, relheight=0.1)

        # Linha 2
        self.nome = Entry(janela, font=("Times New Roman", 15))
        self.nome.place(relx=0.01, rely=0.12, relwidth=0.97, relheight=0.1)
        self.nome.insert(0, nome)

        # Linha 3
        Label(janela, text='CPF:', font=("Times New Roman", 15)).place(relx=0, rely=0.24, relwidth=0.1, relheight=0.1)

        self.cpf = Entry(janela, font=("Times New Roman", 15))
        self.cpf.place(relx=0.11, rely=0.24, relwidth=0.3, relheight=0.1)
        self.cpf.insert(0, cpf)
        self.cpf.config(state = 'disabled')

        Label(janela, text='Telefone:', font=("Times New Roman", 15)).place(relx=0.40, rely=0.24, relwidth=0.3, relheight=0.1)

        self.ddd = Entry(janela, font=("Times New Roman", 15))
        self.ddd.place(relx=0.66, rely=0.24, relwidth=0.07, relheight=0.1)
        self.ddd.insert(0, ddd)

        self.numero = Entry(janela, font=("Times New Roman", 15))
        self.numero.place(relx=0.75, rely=0.24, relwidth=0.23, relheight=0.1)
        self.numero.insert(0, numero)

        # Linha 4
        Label(janela, text='Nome da Equipe:', font=("Times New Roman", 15)).place(relx=0, rely=0.36, relwidth=0.3,
                                                                          relheight=0.1)
        # Linha 5
        self.equipe = Entry(janela, font=("Times New Roman", 15))
        self.equipe.place(relx=0.01, rely=0.48, relwidth=0.97, relheight=0.1)
        self.equipe.insert(0, equipe)

        # Linha 6
        Label(janela, text='Turno:', font=("Times New Roman", 15)).place(relx=0, rely=0.6, relwidth=0.1, relheight=0.1)
        self.escolha = ttk.Combobox(janela, textvariable=StringVar())
        self.escolha['values'] = ('Manhã', 'Tarde', 'Noite')
        self.escolha.place(relx=0.12, rely=0.6, relwidth=0.3, relheight=0.1)
        self.escolha.insert(0, turno)

        # Linha 7
        self.bt_salvar = Button(janela, text='Salvar', font=("Times New Roman", 15), command= self.salvar)
        self.bt_salvar.place(relx=0.05, rely=0.78, relwidth=0.25, relheight=0.1)

        self.bt_limpar = Button(janela, text='Limpar', font=("Times New Roman", 15), command= self.limpar)
        self.bt_limpar.place(relx=0.375, rely=0.78, relwidth=0.25, relheight=0.1)

        self.bt_cancelar = Button(janela, text='Cancelar', font=("Times New Roman", 15), command=janela.destroy)
        self.bt_cancelar.place(relx=0.7, rely=0.78, relwidth=0.25, relheight=0.1)

    def salvar(self):
        if messagebox.askyesno('Verificar', 'Realmente quer alterar estes dados?'):
            try:
                nome = self.nome.get()
                cpf = self.cpf.get()
                ddd = self.ddd.get()
                numero = self.numero.get()
                equipe = self.equipe.get()
                escolha = self.escolha.get()
                if nome and cpf and ddd and numero and equipe and escolha != '':
                    if len(numero) == 8 and numero[0] == '3':
                        telefone = ddd + ' ' + numero[0:4] + '-' + numero[4:8]
                        self.banco_tecnicos.inserir_dados(cpf, nome, telefone, escolha, equipe)
                        messagebox.showwarning('Yes', 'As modificações foram salvas')
                    elif len(numero) == 9 and numero[0] == '9':
                        telefone = ddd + ' ' + numero[0:5] + '-' + numero[5:9]
                        self.banco_tecnicos.atualizar_dados(cpf, nome, telefone, escolha, equipe)
                        messagebox.showwarning('Yes', 'As modificações foram salvas')
                    else:
                        texto = 'Número informado inválido'
                        messagebox.showinfo('Alerta!!!', texto)
                else:
                    texto = 'Existem campos não preenchidos'
                    messagebox.showinfo('Alerta!!!', texto)
            except:
                print('Não foi possível slavar as alterações')

    def limpar(self):
        try:
            self.nome.delete(0, END)
            self.ddd.delete(0, END)
            self.numero.delete(0, END)
            self.equipe.delete(0, END)
            self.escolha.delete(0, END)
            print('Campos limpos')
        except:
            print('Não foi possível limpar os campos')