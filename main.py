from tkinter import *
import settings
import calculos
from campo import Campo

root = Tk()
root.configure(bg= "grey")
root.geometry(f'{settings.LARGURA}x{settings.ALTURA}')
root.title("Campo Minado")
root.resizable(False, False)

titulo_frame = Frame(root, bg= "grey",
                      width= settings.LARGURA, 
                      height= calculos.definir_altura(20))
titulo_frame.place(x = 0,y = 0)

contador_frame = Frame(root, bg= "grey",
                        width= calculos.definir_largura(25), 
                        height= calculos.definir_altura(75))
contador_frame.place(x = 0, y = calculos.definir_altura(20))

campo_frame = Frame(root, bg= "grey",
                    width= calculos.definir_largura(75), 
                    height= calculos.definir_altura(75))
campo_frame.place(x = calculos.definir_largura(25), y = calculos.definir_altura(20))

for x in range(settings.TAMANHO_CAMPO):
    for y in range(settings.TAMANHO_CAMPO):
        c1 = Campo()
        c1.cria_botao(campo_frame)
        c1.botao.grid(column= x, row= y)


#Roda a aba
root.mainloop()