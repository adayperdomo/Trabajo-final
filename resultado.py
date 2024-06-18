class Resultado:
    def __init__(self, resultado) -> None:
        self.resultado = resultado

    def __str__(self) -> str:
        return self.resultado
    
    def leer(self) -> str:
        return self.resultado