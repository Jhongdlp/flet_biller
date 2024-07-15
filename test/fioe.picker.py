import flet as ft


def main(page: ft.Page):
    page.title = "Cambiar Imagen con FilePicker"

    # Imagen inicial
    imagen_actual = "https://placehold.co/600x400"

    # Contenedor para la imagen
    contenedor_imagen = ft.Container(
        content=ft.Image(
            src=imagen_actual,
            width=600,
            height=400,
            fit=ft.ImageFit.COVER,
        ),
    )

    # FilePicker
    def seleccionar_imagen(e: ft.FilePickerResultEvent):
        if e.files:
            archivo = e.files[0]
            contenedor_imagen.content.src = archivo.path  # Actualiza con la ruta del archivo
            page.update()

    selector_archivo = ft.FilePicker(on_result=seleccionar_imagen)
    page.overlay.append(selector_archivo)  # Agrega el FilePicker a la página

    def abrir_selector(e):
        selector_archivo.pick_files(
            allowed_extensions=["png", "jpg", "jpeg"],  # Filtra por extensiones
            dialog_title="Selecciona una imagen",
        )

    # Botón para abrir el FilePicker
    boton_cambiar = ft.ElevatedButton("Cambiar Imagen", on_click=abrir_selector)

    # Agrega los controles a la página
    page.add(
        contenedor_imagen,
        boton_cambiar,
    )


ft.app(target=main)