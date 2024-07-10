import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            [
                ft.Text("Dirección"),
                ft.Container(
                    content=ft.TextArea(
                        hint_text="Dirección del cliente",
                        min_lines=3, # Controla la altura visible
                        height=100, # Define la altura fija
                    ),
                    border_radius=ft.border_radius.all(5), # Para un aspecto más similar al TextField
                    border=ft.border.all(1, ft.colors.GREY_400), # Añade un borde
                    padding=10,
                )
            ]
        )
    )

ft.app(target=main)