import settings

def definir_altura(porcentagem):
    return (settings.ALTURA / 100) * porcentagem

def definir_largura(porcentagem):
    return (settings.LARGURA / 100) * porcentagem