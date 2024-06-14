from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static

from textual.binding import Binding
from textual.widgets import Footer 
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Input
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
            self.app.switch_to_main()

        elif event.button.id == "adios":      
            self.exit(str(event.button))

class Main():
    

if __name__ == "__main__":
    app = InputApp()
    print(app.run())