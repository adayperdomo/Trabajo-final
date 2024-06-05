class Partido:
    def __init__(self, partido) -> None:
        self.partido = partido

    def __str__(self) -> str:
        return self.partido
    
    def leer(self) -> str:
        return self.partido