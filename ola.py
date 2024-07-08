import flet as ft

# Función para crear contenido de la página
def create_page_content(page_name):
    return ft.Column(
        controls=[
            ft.Text(f"Esta es la {page_name}")
        ]
    )

# Función principal
def main(page: ft.Page):
    # Función de navegación
    def navigate(page_name):
        page.go(f"/{page_name}")
    
    # Crear el rail (barra lateral)
    rail = ft.NavigationRail(
        selected_index=0,
        height=700,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="Settings"),
            ft.NavigationRailDestination(icon=ft.icons.INFO, label="Info"),
        ],
        on_change=lambda e: navigate(["home", "settings", "info"][e.control.selected_index])
    )

    # Contenedor para las páginas
    page_container = ft.Container(expand=True)

    # Función para actualizar el contenido de la página
    def on_route_change(route):
        page_name = route.route.strip("/")
        page_container.content = create_page_content(page_name)
        page.update()

    # Configurar el manejador de cambios de ruta
    page.on_route_change = on_route_change

    # Layout principal
    page.add(
        ft.Row(
            controls=[
                rail,
                page_container
            ]
        )
    )

    # Navegar a la página inicial
    page.go("/home")

# Ejecutar la aplicación
ft.app(target=main)
