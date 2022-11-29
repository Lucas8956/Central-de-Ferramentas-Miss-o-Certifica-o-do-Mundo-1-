from tkinter import *
import janela_tecnico
import janela_ferr
import janela_res

class Principal:
    def __init__(self, janela):
        # Construção da janela
        self.bt_tecnicos = Button(janela, text='Técnicos', font=('bold'), command= self.tela_tecnicos)
        self.bt_tecnicos.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.2)

        self.bt_ferramentas = Button(janela, text='Ferramentas', font=('bold'), command= self.tela_ferramentas)
        self.bt_ferramentas.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.2)

        self.bt_reservas = Button(janela, text='Reservas', font=('bold'), command= self.tela_reservas)
        self.bt_reservas.place(relx=0.05, rely=0.35, relwidth=0.4, relheight=0.2)

        self.bt_sobre = Button(janela, text='Sobre', font=('bold'), command= self.tela_sobre)
        self.bt_sobre.place(relx=0.55, rely=0.35, relwidth=0.4, relheight=0.2)

        self.bt_sair = Button(janela, text='Sair', font=('bold'), command=janela.destroy)
        self.bt_sair.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.2)

    def tela_tecnicos(self):
        try:
            self.janela_tec = Toplevel()
            self.janela_tec.focus_force()
            self.janela_tec.grab_set()
            #self.janela_tec.transient(janela)
            self.interface_tec = janela_tecnico.Tecnicos_GUI(self.janela_tec)
        except:
            print('Não possível abrir a janela')

    def tela_ferramentas(self):
        try:
            self.janela_ferr = Toplevel()
            self.janela_ferr.focus_force()
            self.janela_ferr.grab_set()
            #self.janela_ferr.transient(janela)
            self.interface_ferr = janela_ferr.Ferraments_GUI(self.janela_ferr)
        except:
            print('Não foi possível abrir janela')

    def tela_reservas(self):
        try:
            self.janela_reserva = Toplevel()
            self.janela_reserva.focus_force()
            self.janela_reserva.grab_set()
            #self.janela_reserva.transient(janela)
            self.interface_res = janela_res.Reservas_GUI(self.janela_reserva)
        except:
            print('Não foi possível abrir janela')

    def tela_sobre(self):
        try:
            self.janela_logo = Toplevel()
            self.janela_logo.focus_force()
            self.janela_logo.grab_set()

            self.janela_logo.geometry("600x250")
            self.janela_logo.resizable(False, False)

            self.logo = PhotoImage(file=r"C:\Users\lucas\Downloads\2.png")

            label1 = Label(self.janela_logo, image=self.logo)
            label1.place(x=0, y=0)

            label2 = Label(self.janela_logo, font=("Times New Roman", 15), text='Trabalho do Curso')
            label2.place(relx=0.55, rely=0.02, relwidth=0.4, relheight=0.2)

            label3 = Label(self.janela_logo, font=("Times New Roman", 15), text='Desenvolvimento Full-Stack')
            label3.place(relx=0.55, rely=0.2, relwidth=0.45, relheight=0.2)

            label4 = Label(self.janela_logo, font=("Times New Roman", 15), text='Aluno:')
            label4.place(relx=0.7, rely=0.4, relwidth=0.1, relheight=0.2)

            label5 = Label(self.janela_logo, font=("Times New Roman", 15), text='Lucas Figueirêdo Costa de Queiroz')
            label5.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.2)
        except:
            print('Não foi possível abrir a janela')

janela = Tk()
janela.geometry('400x200')
janela.resizable(False, False)
janela.title('Central de Ferramentas')
interface = Principal(janela)
janela.mainloop()