from tkinter import *
import settings
import calculos
from campo import Campo

root = Tk()
root.configure(bg= "black")
root.geometry(f'{settings.LARGURA}x{settings.ALTURA}')
root.title("Campo Minado")
root.resizable(False, False)

titulo_frame = Frame(root, bg= "black",
                      width= settings.LARGURA, 
                      height= calculos.definir_altura(20))
titulo_frame.place(x = 0,y = 0)
titulo = Label(titulo_frame, bg= "black", fg= "white", text= 'Campo Minado', font= ("", 70))
titulo.place(x= 320, y= 30)
contador_frame = Frame(root, bg= "black",
                        width= calculos.definir_largura(25), 
                        height= calculos.definir_altura(75))
contador_frame.place(x = 0, y = calculos.definir_altura(20))

campo_frame = Frame(root, bg= "black",
                    width= calculos.definir_largura(75), 
                    height= calculos.definir_altura(75))
campo_frame.place(x = calculos.definir_largura(25), y = calculos.definir_altura(20))

for y in range(settings.TAMANHO_CAMPO):
    for x in range(settings.TAMANHO_CAMPO):
        c1 = Campo(x, y)
        c1.cria_botao(campo_frame)
        c1.botao.grid(column= x, row= y)

Campo.cria_contadores(contador_frame)
Campo.contador.place(x= 0, y= 0)
botao_reiniciar = Button(contador_frame, text="Reiniciar", 
                                 width= 12, height= 2)
botao_reiniciar.bind('<Button-1>', lambda event: Campo.reiniciar_jogo(campo_frame))
botao_reiniciar.place(x= 80, y= 200)

#Roda a aba
root.mainloop()