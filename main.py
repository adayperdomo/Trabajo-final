from coleccionApuesta import ColeccionApuestas
from apuesta import Apuesta

ca = ColeccionApuestas()
#print(ca.leer())
#ca.buscar(Cita(''))

print(ca.buscar(Apuesta('')))
print(ca.insertar(Apuesta('')))
ca.borrar(Apuesta(''))
ca.actualizar('')
print(ca.leer())
