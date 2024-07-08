import flet as ft
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.info import InfoPage

# Función principal
def main(page: ft.Page):
    # Contenedor para las páginas
    page_container = ft.Container(expand=True)

    # Función para actualizar el contenido de la página
    def on_route_change(route):
        page_name = route.route.strip("/")
        if page_name == "home":
            page_container.content = HomePage(page)
        elif page_name == "settings":
            page_container.content = SettingsPage(page)
        elif page_name == "info":
            page_container.content = InfoPage(page)
        page.update()

    # Configurar el manejador de cambios de ruta
    page.on_route_change = on_route_change

    # Layout principal
    page.add(page_container)

    # Navegar a la página inicial
    page.go("/home")

# Ejecutar la aplicación
ft.app(target=main)
