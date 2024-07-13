import flet as ft

def main(page: ft.Page):
    # Definir los campos de texto sin error inicial
    nombre_field = ft.TextField(
        label="Nombre",
        error_text=None,  # No mostrar error inicialmente
    )

    apellido_field = ft.TextField(
        label="Apellido",
        error_text=None,  # No mostrar error inicialmente
    )

    text_field = ft.TextField(
        label="Introduce algo",
        error_text=None,  # No mostrar error inicialmente
    )

    # Definir la función que se ejecutará al presionar el botón
    def on_click(e):
        # Validar todos los campos
        error = False
        if not nombre_field.value:
            nombre_field.error_text = "Este campo es obligatorio"
            nombre_field.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True

        if not apellido_field.value:
            apellido_field.error_text = "Este campo es obligatorio"
            apellido_field.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True

        if not text_field.value:
            text_field.error_text = "Este campo es obligatorio"
            text_field.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True

        if error:
            nombre_field.update()
            apellido_field.update()
            text_field.update()
        else:
            # Mostrar el contenido de todos los campos
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    f"Nombre: {nombre_field.value}, Apellido: {apellido_field.value}, Contenido: {text_field.value}"
                )
            )
            page.snack_bar.open = True
            nombre_field.error_text = None
            apellido_field.error_text = None
            text_field.error_text = None
            page.update()

    # Definir la función que se ejecutará al cambiar el texto
    def on_change(e):
        if nombre_field.error_text:
            nombre_field.error_text = None
            nombre_field.update()

        if apellido_field.error_text:
            apellido_field.error_text = None
            apellido_field.update()

        if text_field.error_text:
            text_field.error_text = None
            text_field.update()

    # Asociar la función on_change al evento on_change de los TextField
    nombre_field.on_change = on_change
    apellido_field.on_change = on_change
    text_field.on_change = on_change

    # Definir el botón
    button = ft.ElevatedButton(text="Mostrar contenido", on_click=on_click)

    # Añadir los controles a la página
    page.add(nombre_field, apellido_field, text_field, button)

# Ejecutar la aplicación Flet
ft.app(target=main)
