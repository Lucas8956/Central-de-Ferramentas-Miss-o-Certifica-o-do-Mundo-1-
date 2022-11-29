from tkinter import *
import ferramentas as ferr
from tkinter import messagebox

class Ferr_Cadastro_GII:
    def __init__(self, janela):
        self.banco_ferr = ferr.Ferramentas_BD()
        print('Método construtor chamado')

        ### Construção da janela
        janela.geometry('600x400')
        janela.resizable(False, False)
        janela.title('Cadastro de Ferramentas')

        # Linha1
        Label(janela, text='Descrição da Ferramenta:', font=("Times New Roman", 15)).place(relx=0, rely=0,
                                                                                           relwidth=0.36,
                                                                                           relheight=0.08)
        # Linha 2
        self.txt_descricao = Entry(janela, font=("Times New Roman", 15))
        self.txt_descricao.place(relx=0.01, rely=0.08, relwidth=0.98, relheight=0.08)

        # Linha 3
        Label(janela, text='Fabricante:', font=("Times New Roman", 15)).place(relx=0, rely=0.18, relwidth=0.17,
                                                                              relheight=0.08)
        self.txt_fabricante = Entry(janela, font=("Times New Roman", 15))
        self.txt_fabricante.place(relx=0.18, rely=0.18, relwidth=0.8, relheight=0.08)

        # Linha 4
        Label(janela, text='Part_Number:', font=("Times New Roman", 15)).place(relx=0, rely=0.28, relwidth=0.2,
                                                                               relheight=0.08)
        self.txt_part_number = Entry(janela, font=("Times New Roman", 15))
        self.txt_part_number.place(relx=0.21, rely=0.28, relwidth=0.27, relheight=0.08)
        Label(janela, text='Voltagem:', font=("Times New Roman", 15)).place(relx=0.51, rely=0.28, relwidth=0.17,
                                                                            relheight=0.08)
        self.txt_voltagem = Entry(janela, font=("Times New Roman", 15))
        self.txt_voltagem.place(relx=0.69, rely=0.28, relwidth=0.29, relheight=0.08)

        # Linha 5
        Label(janela, text='Tamanho:', font=("Times New Roman", 15)).place(relx=0, rely=0.38, relwidth=0.14,
                                                                           relheight=0.08)
        self.txt_tamanho = Entry(janela, font=("Times New Roman", 15))
        self.txt_tamanho.place(relx=0.21, rely=0.38, relwidth=0.26)
        Label(janela, text='Unidade de Medida:', font=("Times New Roman", 15)).place(relx=0.51, rely=0.38, relwidth=0.3,
                                                                                     relheight=0.08)
        self.txt_un_medida = Entry(janela, font=("Times New Roman", 15))
        self.txt_un_medida.place(relx=0.82, rely=0.38, relwidth=0.16, relheight=0.08)

        # Linha 6
        Label(janela, text='Tipo de Ferramenta:', font=("Times New Roman", 15)).place(relx=0, rely=0.48, relwidth=0.28,
                                                                                      relheight=0.08)
        self.txt_tipo = Entry(janela, font=("Times New Roman", 15))
        self.txt_tipo.place(relx=0.29, rely=0.48, relwidth=0.67, relheight=0.08)

        # Linha 7
        Label(janela, text='Material da Ferramenta:', font=("Times New Roman", 15)).place(relx=0, rely=0.58,
                                                                                          relwidth=0.33, relheight=0.08)
        self.txt_material = Entry(janela, font=("Times New Roman", 15))
        self.txt_material.place(relx=0.34, rely=0.58, relwidth=0.64, relheight=0.08)

        # Linha 8
        Label(janela, text='Tempo Máximo de Reserva da Ferramenta (em horas):', font=("Times New Roman", 15)).place(
            relx=0, rely=0.68, relwidth=0.73, relheight=0.08)
        self.txt_tempo_max_res = Entry(janela, font=("Times New Roman", 15))
        self.txt_tempo_max_res.place(relx=0.74, rely=0.68, relwidth=0.23, relheight=0.08)

        # Linha 9
        self.bt_limpar = Button(janela, text='Limpar', font=("Times New Roman", 15), command = self.limpar)
        self.bt_limpar.place(relx=0.83, rely=0.78, relwidth=0.15, relheight=0.08)

        # Linha 10
        self.bt_cadastrar = Button(janela, text='Cadastrar', font=("Times New Roman", 15), command = self.cadastrar)
        self.bt_cadastrar.place(relx=0.01, rely=0.88, relwidth=0.15, relheight=0.08)
        self.bt_cancelar = Button(janela, text='Cancelar', font=("Times New Roman", 15), command = janela.destroy)
        self.bt_cancelar.place(relx=0.83, rely=0.88, relwidth=0.15, relheight=0.08)

    def cadastrar(self):
        try:
            descricao = self.txt_descricao.get()
            fabricante = self.txt_fabricante.get()
            voltagem = self.txt_voltagem.get()
            part_number = self.txt_part_number.get()
            tamanho = self.txt_tamanho.get()
            un_medida = self.txt_un_medida.get()
            tipo = self.txt_tipo.get()
            material = self.txt_material.get()
            tempo_max_res = self.txt_tempo_max_res.get()
            if descricao and fabricante and part_number and tamanho and un_medida and tipo and material and tempo_max_res != '':
                tempo_max_res = int(tempo_max_res)
                self.banco_ferr.inserir_dados(descricao, fabricante, voltagem, part_number, tamanho, un_medida, tipo, material, tempo_max_res)
            else:
                texto = 'Campos Descrição, Fabricante, Part_number, Tamanho, Tipo de Ferramenta, Materiale e Tempo de Reserva são de preenchimento obrigatório'
                messagebox.showinfo('Alerta!!!', texto)
        except:
            print('Não foi possível concluir o cadastro')

    def limpar(self):
        try:
            self.txt_descricao.delete(0, END)
            self.txt_fabricante.delete(0, END)
            self.txt_voltagem.delete(0, END)
            self.txt_part_number.delete(0, END)
            self.txt_tamanho.delete(0, END)
            self.txt_un_medida.delete(0, END)
            self.txt_tipo.delete(0, END)
            self.txt_material.delete(0, END)
            self.txt_tempo_max_res.delete(0, END)
            print('Campos limpos')
        except:
            print('Não foi possível limpar os campos')