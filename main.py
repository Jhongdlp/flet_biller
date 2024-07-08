import flet as ft
from pages.home import HomePage
from pages.views.generar_bd import inventario_page
from pages.login_page import Login_page
from pages.views.add_pro_page import generar_factura_pro
from pages.Registro import RegistroPage
# Función principal
def main(page: ft.Page):
    # Contenedor para las páginas
    page_container = ft.Container(expand=True)

    # Función para actualizar el contenido de la página
    def on_route_change(route):
        page_name = route.route.strip("/")

        if page_name == "":
            page_container.content = Login_page(page)

        elif page_name == "registro":
            page_container.content = RegistroPage(page)

        elif page_name == "home":
            page_container.content = HomePage(page)
            
        elif page_name == "inventario":
            page_container.content = inventario_page(page)

        elif page_name == "generar_facturas":
            page_container.content = generar_factura_pro(page)


        page.update()

    # Configurar el manejador de cambios de ruta
    page.on_route_change = on_route_change

    # Layout principal
    page.add(page_container)

    # Navegar a la página inicial
    page.go("/generar_facturas")

# Ejecutar la aplicación
ft.app(target=main)
