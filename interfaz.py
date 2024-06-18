from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Header
from textual.widgets import Footer 
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Input


from coleccionApuesta import ColeccionApuestas
from apuesta import Apuesta
from coleccionResultado import ColeccionResultados
from resultado import Resultado
from coleccionPartido import ColeccionPartidos
from partido import Partido

class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"


class InputApp(App):
    def compose(self) -> ComposeResult:

        yield Vertical(
                Input(placeholder="Nombre"),
                Input(placeholder="Dinero para apostar"),
                Button("Comenzar la apuesta", id="aceptar"),
                Button.error("Salir", id="adios"),
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "aceptar":
            self.app.push_screen(ApostarScreen())

        elif event.button.id == "adios":      
            self.exit(str(event.button))

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Apostar", id="apostar"),
            Button("Partido", id="partido"),
            Button("Resultado", id="resultado"),
            Button.error("Salir", id="adios"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "apostar":
            self.app.push_screen(ApostarScreen())
        elif event.button.id == "partido":
            self.app.push_screen(PartidoScreen())
        elif event.button.id == "resultado":
            self.app.push_screen(ResultadoScreen())
        elif event.button.id == "adios":
            self.app.exit(str(event.button))    

class ApostarScreen(Screen):
    def compose(self) -> ComposeResult:
        
        yield Horizontal(
            Input(placeholder="Un número positivo", id="numero"),
        )

        yield Horizontal(
            Button("Aceptar", id="aceptar"),
            Button("Insertar", id="insertar"),
            Button("Borrar", id="borrar"),
            Button("Volver", id="volver"),
            Button.error("Salir", id="adios"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.push_screen(MainScreen())
        elif event.button.id == "insertar":
            self.app.mytable = "apostar"
            self.app.pop_screen()
            self.app.push_screen(InsertarScreen())
        elif event.button.id == "borrar":
            self.app.mytable = "apostar"
            self.app.pop_screen()
            self.app.push_screen(BorrarScreen())
        elif event.button.id == "aceptar":
            self.app.pop_screen()
            self.app.push_screen(PartidoScreen())

class PartidoScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Comenzar partido", id="comienzo"),
            Button("Insertar", id="insertar"),
            Button("Borrar", id="borrar"),
            Button("Volver", id="volver"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.push_screen(MainScreen())
        elif event.button.id == "insertar":

            self.app.pop_screen()
            self.app.push_screen(InsertarScreen())
        elif event.button.id == "borrar":
            self.app.pop_screen()
            self.app.push_screen(BorrarScreen())
        elif event.button.id == "comienzo":
            self.app.pop_screen()
            self.app.push_screen(ResultadoScreen())

class ResultadoScreen():
    def compose(self) -> ComposeResult:
        yield Button("Insertar", id="insertar")
        yield Button("Borrar", id="borrar")
        yield Button("Volver", id="volver")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.push_screen(MainScreen())
        elif event.button.id == "insertar":
            self.app.pop_screen()
            self.app.push_screen(InsertarScreen())
        elif event.button.id == "borrar":
            self.app.pop_screen()
            self.app.push_screen(BorrarScreen())

class InsertarScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Insertar datos") 
        yield Input(placeholder="")
        yield Button("Volver", id="volver")
        yield Button("Aceptar", id="aceptar")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.pop_screen()
        elif event.button.id == "aceptar" and self.app.mytable == "apuesta":
            self.app.ca.insertar(Apuesta(self.query_one(Input).value))
        elif event.button.id == "aceptar" and self.app.mytable == "partido":
            self.app.ct.insertar(Partido(self.query_one(Input).value))
        elif event.button.id == "aceptar" and self.app.mytable == "resultado":
            self.app.ch.insertar(Resultado(self.query_one(Input).value))

    def _on_mount(self) -> None:
        self.title = "Insertar datos"


class BorrarScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Borrar datos") 
        yield Input(placeholder="")
        yield Button("Volver", id="volver")
        yield Button("Aceptar", id="aceptar")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.pop_screen()
        elif event.button.id == "aceptar" and self.app.mytable == "apuesta":
            self.app.ca.borrar(Apuesta(self.query_one(Input).value))
        elif event.button.id == "aceptar" and self.app.mytable == "partido":
            self.app.ct.borrar(Partido(self.query_one(Input).value))
        elif event.button.id == "aceptar" and self.app.mytable == "resultado":
            self.app.ch.borrar(Resultado(self.query_one(Input).value))  

    def _on_mount(self) -> None:
        self.title = "Borrar datos"


if __name__ == "__main__":
    app = InputApp()
    print(app.run())

