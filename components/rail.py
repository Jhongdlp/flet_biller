import flet as ft

def create_navigation_rail(page: ft.Page, selected_index: int):
    rail = ft.NavigationRail(
        width=120,
        height=700,
        bgcolor=ft.colors.TRANSPARENT,
        selected_index=selected_index,
        label_type=ft.NavigationRailLabelType.ALL,
        indicator_shape=ft.StadiumBorder(),
        #elevation=20,
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED, 
                selected_icon=ft.icons.HOME, 
                label="Menu principal",padding=13 
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SHOPPING_CART_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.SHOPPING_CART_ROUNDED),
                label="Facturas",padding=15
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.ADD_ROUNDED),
                label_content=ft.Text("Generar facturas"),padding=13
            ),
            ft.NavigationRailDestination(
                selected_icon=ft.icons.GROUP_ROUNDED,
                icon=ft.icons.GROUP_OUTLINED,
                label_content=ft.Text("Clientes"),padding=13
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INVENTORY_2_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.INVENTORY_2_ROUNDED),
                label_content=ft.Text("Inventario"),padding=13
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.QUERY_STATS_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.QUERY_STATS_ROUNDED),
                label_content=ft.Text("Estadisticas"),padding=13
            ),
        ],
        on_change=lambda e: page.go(["/home", "/Facturas", "/generar_facturas","/Clientes","/Inventario","/Estadistica"][e.control.selected_index])
    )
    return rail
