from db import Db
from apostador import Apostador

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS apostador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    apostador TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM apostadores
'''

SQLDDLINSERT =  '''INSERT INTO apostadores (apostador) VALUES'''
                #Hay que concatenar ('apostador')


SQLDDLUPDATEPART1 = '''UPDATE apostadores SET apostador = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM apostadores WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM apostadores WHERE apostador LIKE '''
                #Hay que concatenar


class ColeccionApostadores:
    DBNAME = 'apostadores.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, apostador):
        if self.buscar(apostador) == 0:
            elstr = "('" + str(apostador) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldapostadores:str, newapostadores:str):
        id = self.buscar(oldapostadores)
        if id != 0:
            elstr = SQLDDLUPDATEPART1 + newapostadores 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, apostador):
        id = self.buscar(apostador) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, apostador:Apostador) -> int:
        resultado = 0
        elstr = '"' + str(apostador) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado