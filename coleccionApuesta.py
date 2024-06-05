from db import Db
from apuesta import Apuesta

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS apuestas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	apuesta TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM apuestas
'''

SQLDDLINSERT = '''INSERT INTO apuestas (apuesta) VALUES '''
                #Hay que concatenar  ('apuesta')

SQLDDLUPDATEPART1 = '''UPDATE apuestas SET apuesta = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM apuestas WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM apuestas WHERE apuesta LIKE '''
                #Hay que concatenar



class ColeccionApuestas:
    DBNAME = 'apuestas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, apuesta):
        if self.buscar(apuesta) == 0:
            elstr = "('" + str(apuesta) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldApuestas:str, newApuestas:str):
        id = self.buscar(oldApuestas)
        if id != 0:
            elstr = SQLDDLUPDATEPART1 + newApuestas 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, apuesta):
        id = self.buscar(apuesta) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, apuesta:Apuesta) -> int:
        resultado = 0
        elstr = '"' + str(apuesta) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado