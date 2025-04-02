class DesarrolloDeComputacion():
    
    def escribe_fichero(self, mensaje):
        with open('fichero_comunicacion.txt', 'a') as fichero:
            fichero.writelines(mensaje)


    def lee_fichero(selfA):
        mensaje=""
        with open('fichero_comunicacion.txt', 'r') as fichero:
            mensaje = fichero.read()
        return mensaje
    

nombre = input('¿Cual es tu nombre? ')
comida = input('cuales_tu_comida_favorita?')
edad = input('¿Cual es tu edad?')

mi_lista=[nombre+'\n',comida+'\n',edad+'\n']

descom = DesarrolloDeComputacion()
descom.escribe_fichero(mi_lista)
print(descom.lee_fichero())