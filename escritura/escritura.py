
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.writelines(mensaje)


def lee_fichero():
    mensaje=""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    return mensaje
    

nombre = input('¿Cual es tu nombre? ')
comida = input('cuales_tu_comida_favorita?')
edad = input('¿Cual es tu edad?')

mi_lista=[nombre+'\n',comida+'\n',edad+'\n']


escribe_fichero(mi_lista)
print(lee_fichero())