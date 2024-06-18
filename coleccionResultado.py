from db import Db
from resultado import Resultado

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS resultado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resultado TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM resultados
'''

SQLDDLINSERT =  '''INSERT INTO resultados (resultado) VALUES'''
                #Hay que concatenar ('resultado')


SQLDDLUPDATEPART1 = '''UPDATE resultados SET resultado = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM resultados WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM resultados WHERE resultado LIKE '''
                #Hay que concatenar


class ColeccionResultados:
    DBNAME = 'resultados.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, resultado):
        if self.buscar(resultado) == 0:
            elstr = "('" + str(resultado) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldresultadoes:str, newresultadoes:str):
        id = self.buscar(oldresultadoes)
        if id != 0:
            elstr = SQLDDLUPDATEPART1 + newresultadoes 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, resultado):
        id = self.buscar(resultado) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, resultado:Resultado) -> int:
        resultado = 0
        elstr = '"' + str(resultado) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado