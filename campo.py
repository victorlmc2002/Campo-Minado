from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Campo:
    todos = []
    criado = False
    qtd_minas = 0
    qtd_campos = settings.QTD_CAMPOS
    contador = None

    def __init__(self,x, y, flag_mina = False):
        self.flag_mina= flag_mina
        self.botao = None
        self.x = x
        self.y = y
        self.ja_verificado = False

        Campo.todos.append(self)

    def cria_botao(self, posicao):
        btn = Button(posicao,width= 8, height= 2)
        btn.bind('<Button-1>', self.checar_campo)
        btn.bind('<Button-3>', self.marcar_campo)
        self.botao = btn

    @staticmethod    
    def cria_contadores(posicao):
        contador = Label(posicao, bg= "black", fg= "white",
                          text= f"Falta {settings.QTD_CAMPOS} campos", font= ("", 30))
        Campo.contador = contador
    
    def checar_campo(self, event=None):
        if Campo.criado == False:
            Campo.cria_minas()
            if self.flag_mina:
                    Campo.qtd_minas -= 1
            self.flag_mina = False
            for campo in self.minas_proximas:
                if campo.flag_mina:
                    Campo.qtd_minas -= 1
                campo.flag_mina = False
            Campo.criado = True
        if self.ja_verificado:
            return
        if self.flag_mina:
            self.perdeu_jogo()
        else:
            Campo.qtd_campos -= 1
            self.ja_verificado = True
            if self.qtd_minas_prox == 0:
                for campo in self.minas_proximas:
                    campo.checar_campo()
            self.botao.configure(text=f"{self.qtd_minas_prox}")
            self.botao.configure(bg= "azure3")
            if(Campo.contador and Campo.qtd_minas):
                Campo.contador.configure(text= f"Falta {Campo.qtd_campos} campos\n{Campo.qtd_minas} minas")

    def obtem_campo_coordenadas(self, x, y):
        for campo in Campo.todos:
            if campo.x == x and campo.y == y:
                return campo

    @property
    def minas_proximas(self):
        campos_rodeando = [self.obtem_campo_coordenadas(self.x - 1, self.y - 1),
                           self.obtem_campo_coordenadas(self.x - 1, self.y),
                           self.obtem_campo_coordenadas(self.x - 1, self.y + 1),
                           self.obtem_campo_coordenadas(self.x, self.y - 1),
                           self.obtem_campo_coordenadas(self.x + 1, self.y - 1),
                           self.obtem_campo_coordenadas(self.x + 1, self.y),
                           self.obtem_campo_coordenadas(self.x + 1, self.y + 1),
                           self.obtem_campo_coordenadas(self.x, self.y +1)]
        campos_rodeando = [campo for campo in campos_rodeando if campo is not None]
        return campos_rodeando
    @property
    def qtd_minas_prox(self):
        minas = 0
        for campo in self.minas_proximas:
            if campo.flag_mina:
                minas += 1
        return minas

    def perdeu_jogo(self):
        self.botao.configure(bg= "red")
        ctypes.windll.user32.MessageBoxW(0, 'BOOM!', "GAME OVER", 0)
        sys.exit()

    def marcar_campo(self, event):
        if self.botao.cget("bg") == "orange":
            self.botao.configure(bg= "white")
        else:
            self.botao.configure(bg= "orange")

    def cria_minas():
        minas = random.sample(Campo.todos,settings.QTD_MINAS)
        for mina in minas:
            mina.flag_mina = True
            Campo.qtd_minas += 1

    def __repr__(self):
        return f"Campo ({self.x},{self.y}) {self.flag_mina}"