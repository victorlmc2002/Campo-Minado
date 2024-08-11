from tkinter import Button
class Campo:
    def __init__(self, flag_mina = False):
        self.flag_mina= flag_mina
        self.botao = None

    def cria_botao(self, posicao):
        btn = Button(posicao,width= 12, height= 4, text= "teste")
        btn.bind('<Button-1>', self.checar_campo)
        btn.bind('<Button-3>', self.marcar_campo)
        self.botao = btn

    def checar_campo(self, event):
        print(event)
        print("Esquerda")
    
    def marcar_campo(self, event):
        print(event)
        print("Direita")