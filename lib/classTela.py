from tkinter import *
from tkinter import ttk





cor1 = "#1e1f1e" #preto

class Tela:
    def __init__(self, toplevel):
        self.todos_valores = ''
        self.valor_texto = StringVar()
        toplevel.title('Calculadora')
        toplevel.iconbitmap('icon/icon.ico')
        toplevel.geometry('235x318')
        toplevel.config(bg=cor1)

        self.frame_tela = Frame(toplevel, width=235, height=80, bg=cor1)
        self.frame_tela.grid(row=0, column=0)

        self.frame_corpo = Frame(toplevel, width=235, height=268, bg=cor1)
        self.frame_corpo.grid(row=1, column=0)

        #widgets
        self.lb1 = Label(self.frame_tela, width=15, padx=5, height=2, textvariable=self.valor_texto, font=('Verdana', '18'), relief=FLAT, anchor="e", justify=RIGHT)
        self.lb1.place(x=0, y=4)

        self.b_limpador = Button(self.frame_corpo, command= lambda: self.deletar(), text='C', width=10, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_apagar = Button(self.frame_corpo, command= lambda: self.apagar(), text='<-', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_porcentagem = Button(self.frame_corpo, command= lambda: self.entrar_valores("%"),text='%', width=5, height=2, relief=RAISED, overrelief=RIDGE)

        self.b_divisao = Button(self.frame_corpo, command= lambda: self.entrar_valores("/"), text='/', width=5, height=2, bg='orange', relief=RAISED, overrelief=RIDGE)
        self.b_multiplicação = Button(self.frame_corpo, command= lambda: self.entrar_valores("*"), text='x', width=5, height=2, bg='orange', relief=RAISED, overrelief=RIDGE)
        self.b_soma = Button(self.frame_corpo, command= lambda: self.entrar_valores("+"), text='+', width=5, height=2, bg='orange', relief=RAISED, overrelief=RIDGE)
        self.b_subtração = Button(self.frame_corpo, command= lambda: self.entrar_valores("-"), text='-', width=5, height=2, bg='orange', relief=RAISED, overrelief=RIDGE)
        self.b_result = Button(self.frame_corpo, command= lambda: self.calcular(self.todos_valores), text='=', width=5, height=2, bg='orange', relief=RAISED, overrelief=RIDGE)

        self.b_virgula = Button(self.frame_corpo, command= lambda: self.entrar_valores("."),text=',', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_raiz = Button(self.frame_corpo, text='√', width=5, height=2, relief=RAISED, overrelief=RIDGE)

        self.b_m1 = Button(self.frame_corpo, command= lambda: self.entrar_valores("%"), text='%', width=3, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_m2 = Button(self.frame_corpo, command= lambda: self.entrar_valores("%"), text='%', width=3, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_m3 = Button(self.frame_corpo, command= lambda: self.entrar_valores("%"), text='%', width=3, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_m4 = Button(self.frame_corpo, command= lambda: self.entrar_valores("%"), text='%', width=3, height=2, relief=RAISED, overrelief=RIDGE)




        self.b_n0 = Button(self.frame_corpo, command= lambda: self.entrar_valores("0"), text='0', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n1 = Button(self.frame_corpo, command= lambda: self.entrar_valores("1"), text='1', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n2 = Button(self.frame_corpo, command= lambda: self.entrar_valores("2"), text='2', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n3 = Button(self.frame_corpo, command= lambda: self.entrar_valores("3"), text='3', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n4 = Button(self.frame_corpo, command= lambda: self.entrar_valores("4"), text='4', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n5 = Button(self.frame_corpo, command= lambda: self.entrar_valores("5"), text='5', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n6 = Button(self.frame_corpo, command= lambda: self.entrar_valores("6"), text='6', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n7 = Button(self.frame_corpo, command= lambda: self.entrar_valores("7"), text='7', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n8 = Button(self.frame_corpo, command= lambda: self.entrar_valores("8"), text='8', width=5, height=2, relief=RAISED, overrelief=RIDGE)
        self.b_n9 = Button(self.frame_corpo, command= lambda: self.entrar_valores("9"), text='9', width=5, height=2, relief=RAISED, overrelief=RIDGE)

        #posições na tela
        self.b_limpador.place(x=1, y=0)
        self.b_apagar.place(x=86, y=0)
        self.b_porcentagem.place(x=137, y=0)

        self.b_divisao.place(x=188, y=0)
        self.b_multiplicação.place(x=188, y=47)
        self.b_soma.place(x=188, y=94)
        self.b_subtração.place(x=188, y=141)
        self.b_result.place(x=188, y=188)

        self.b_virgula.place(x=137, y=188)
        self.b_raiz.place(x=36, y=188)

        self.b_n0.place(x=86, y=188)
        self.b_n1.place(x=36, y=141)
        self.b_n2.place(x=86, y=141)
        self.b_n3.place(x=137, y=141)
        self.b_n4.place(x=36, y=94)
        self.b_n5.place(x=86, y=94)
        self.b_n6.place(x=137, y=94)
        self.b_n7.place(x=36, y=47)
        self.b_n8.place(x=86, y=47)
        self.b_n9.place(x=137, y=47)

        self.b_m1.place(x=1, y=47)
        self.b_m2.place(x=1, y=94)
        self.b_m3.place(x=1, y=141)
        self.b_m4.place(x=1, y=188)

        toplevel.bind("<Key>", self.teclas)
        toplevel.bind("<BackSpace>", self.apagar)
        toplevel.bind("<Return>", self.enter)
        
    def teclas(self, event={}):
        if event.char.isnumeric() or event.char in '+*/-.,':
            self.entrar_valores(event.char)
    
    def enter(self, event={}):
        self.calcular(self.todos_valores)

    def entrar_valores(self, valor='0'):
        if self.todos_valores == '' and valor == '0':
            self.valor_texto.set(valor)
            

        else:
            self.todos_valores = self.todos_valores + str(valor)
            self.valor_texto.set(self.todos_valores)

    def calcular(self, valores):
        expressao = valores
        resultado = eval(expressao)
        self.deletar()
        self.entrar_valores(resultado)

    def deletar(self):
        self.todos_valores = ''
        self.entrar_valores()

    def apagar(self, event={}):
        if len(self.todos_valores) <= 1:
            self.deletar()
        else:
            self.todos_valores = self.todos_valores[:-1]
            self.valor_texto.set(self.todos_valores)