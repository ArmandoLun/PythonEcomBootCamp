def todoesnumerico(valor):
    try:
        return valor.isNumeric()
    except:
        return False

def controlRango(valor):
    return (999999 < valor < 100000000)
