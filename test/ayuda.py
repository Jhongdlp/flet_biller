import flet as ft

def main(page: ft.Page):
    # Ruta al archivo del nuevo favicon
    page.favicon = "src/Logo.png" 

    # Resto de tu código para la interfaz de la aplicación
    page.add(
        ft.Text("¡Hola! Este es el contenido de mi aplicación Flet.")
    )

ft.app(target=main) 