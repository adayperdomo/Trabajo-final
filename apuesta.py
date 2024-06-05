class Apuesta:
    def __init__(self, apuesta) -> None:
        self.apuesta = apuesta

    def __str__(self) -> str:
        return self.apuesta
    
    def leer(self) -> str:
        return self.apuesta