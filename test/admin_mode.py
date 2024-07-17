import flet as ft

# Contraseña almacenada en una variable
CORRECT_PASSWORD = "admin123"

def main(page: ft.Page):
    # Función para manejar la verificación de la contraseña
    def verify_password(e):
        if password_field.value == CORRECT_PASSWORD:
            print("Contraseña correcta")
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Usted no tiene permisos para ingresar a este módulo"),
                action="Cerrar"
            )
            page.snack_bar.open = True
            page.update()

    # Campo de texto para la contraseña
    password_field = ft.TextField(
        password=True,
        hint_text="Ingrese la contraseña",
        on_submit=verify_password
    )

    # Función para abrir el diálogo de alerta
    def open_dialog(e):
        page.dialog.open = True
        page.update()

    # Función para cerrar el diálogo de alerta
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    # Botón para abrir el diálogo de alerta
    open_dialog_button = ft.ElevatedButton(
        text="Abrir módulo de administrador",
        on_click=open_dialog
    )

    # Definir el AlertDialog
    dialog = ft.AlertDialog(
        title=ft.Text("Módulo para administrador"),
        content=ft.Container(
            height=100,
            content=ft.Column([password_field,
                ft.Divider(),
                ft.Row([
                    ft.TextButton(text="Cancelar", on_click=close_dialog),
                    ft.TextButton(text="Ingresar", on_click=verify_password)
                ],alignment=ft.MainAxisAlignment.END)
                
            ])
        ),
    )

    # Agregar el diálogo a la página
    page.dialog = dialog

    # Agregar el botón a la página
    page.add(open_dialog_button)

ft.app(target=main)
