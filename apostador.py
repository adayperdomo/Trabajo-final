class Apostador:
    def __init__(self, apostador) -> None:
        self.apostador = apostador

    def __str__(self) -> str:
        return self.apostador
    
    def leer(self) -> str:
        return self.apostador