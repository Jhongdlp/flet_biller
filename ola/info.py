import flet as ft
from components.rail import create_navigation_rail

def InfoPage(page: ft.Page):
    return ft.Row(
        controls=[
            create_navigation_rail(page, selected_index=2),
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.Text("Esta es la página Info")
                    ]
                )
            )
        ]
    )
