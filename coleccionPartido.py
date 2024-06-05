from db import Db
from partido import Partido

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS partido (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	partido TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM partidos
'''

SQLDDLINSERT = '''INSERT INTO partidos (partido) VALUES '''
                #Hay que concatenar  ('partido')

SQLDDLUPDATEPART1 = '''UPDATE partidos SET partido = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM partidos WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM partidos WHERE partido LIKE '''
                #Hay que concatenar



class ColeccionPartidos:
    DBNAME = 'partidos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, partido):
        if self.buscar(partido) == 0:
            elstr = "('" + str(partido) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldPartidos:str, newPartidos:str):
        id = self.buscar(oldPartidos)
        if id != 0:
            elstr = SQLDDLUPDATEPART1 + newPartidos 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, partido):
        id = self.buscar(partido) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, partido:Partido) -> int:
        resultado = 0
        elstr = '"' + str(partido) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado