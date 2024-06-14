from coleccionApuesta import ColeccionApuestas
from apuesta import Apuesta

ca = ColeccionApuestas()
#print(ca.leer())
#ca.buscar(Cita(''))

print(ca.buscar(Apuesta('')))
print(ca.insertar(Apuesta('Apuesta realizada')))
#ca.borrar(Apuesta('Apuesta realizada'))
ca.actualizar('Apuesta realizada', "Otra apuesta")
print(ca.leer())
