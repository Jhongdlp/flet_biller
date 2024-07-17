import flet as ft
from pages.home import HomePage
from pages.login_page import Login_page
from pages.Registro import RegistroPage
from pages.configurar_usuario import view_configurar_usuario

from pages.views.view_inventario import view_inventario_all
from pages.views.view_clientes import view_clientes_all
from pages.views.view_generar_facturas import generar_factura_pro
from pages.views.view_facturas import view_facturas_all
from pages.views.view_estadistica import view_estadistica_all
from pages.views.view_agregar_productos import view_add_pro_all
from pages.views.configuracion import view_configuracion_all
# Función principal
def main(page: ft.Page):
    # Contenedor para las páginas
    page_container = ft.Container(expand=True)
    page.theme_mode=ft.ThemeMode.LIGHT
    # Establecer la pantalla de carga

    
    # Configurar el ícono de la ventana
    page.favicon = "https://i.ibb.co/ZxS6FDs/Logo.png"

    # Función para actualizar el contsenido de la página
    def on_route_change(route):
        page_name = route.route.strip("/")

        if page_name == "":
            page_container.content = Login_page(page)

        elif page_name == "registro":
            page_container.content = RegistroPage(page)

        elif page_name == "home":
            page_container.content = HomePage(page)

        elif page_name == "config_usuario":
            page_container.content = view_configurar_usuario(page)
            
        elif page_name == "Facturas":
            page_container.content = view_facturas_all(page)

        elif page_name == "generar_facturas":
            page_container.content = generar_factura_pro(page)

        elif page_name == "Clientes":
            page_container.content = view_clientes_all(page)

        elif page_name == "Inventario":
            page_container.content = view_inventario_all(page)
        
        elif page_name == "Agregar_productos":
            page_container.content = view_add_pro_all(page)

        elif page_name == "Configuraciones":
            page_container.content = view_configuracion_all(page)

        
        elif page_name == "Estadistica":
            page_container.content = view_estadistica_all(page)

        page.update()

    # Configurar el manejador de cambios de ruta
    page.on_route_change = on_route_change

    # Layout principal
    page.add(page_container)

    # Navegar a la página inicial
    page.go("/")

# Ejecutar la aplicación
ft.app(target=main,view=ft.AppView.WEB_BROWSER)
