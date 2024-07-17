import flet as ft
import pages.home as us
import re  # Importa la biblioteca re para usar expresiones regulares

def view_configurar_usuario(page: ft.Page):
    page.title = "Configurar usuario"
    page.padding = 0

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            boton_dark_light_mode.icon = ft.icons.DARK_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            boton_dark_light_mode.icon = ft.icons.LIGHT_MODE
        page.update()

    boton_dark_light_mode = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        on_click=toggle_theme
    )

    def regresar_al_home(e):
        page.go("/home")

    imagen_actual = "https://i.ibb.co/k8WKhZw/perfil.png"

    contenedor_imagen = ft.Container(
        border_radius=ft.border_radius.all(100),
        content=ft.Image(
            src=imagen_actual,
            width=200,
            height=200,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
        ),
    )

    def seleccionar_imagen(e: ft.FilePickerResultEvent):
        if e.files:
            archivo = e.files[0]
            contenedor_imagen.content.src = archivo.path
            page.update()

    selector_archivo = ft.FilePicker(on_result=seleccionar_imagen)
    page.overlay.append(selector_archivo)

    def abrir_selector(e):
        selector_archivo.pick_files(
            allowed_extensions=["png", "jpg", "jpeg"],
            dialog_title="Selecciona una imagen",
        )

    cedula_campo_texfield = ft.TextField(label="Ingresa tu cédula", height=40, width=180)
    nombres_campo_texfield = ft.TextField(label="Ingresa tus nombres", height=40, width=180)
    apellidos_campo_texfield = ft.TextField(label="Ingresa tus apellidos", height=40, width=180)
    mail_campo_texfield = ft.TextField(label="Ingresa tu mail", height=40, width=180)
    ciudad_campo_texfield = ft.TextField(label="Ingresa tu ciudad", height=40, width=180)

    def validar_email(email):
        """Valida si la cadena de entrada tiene el formato de un correo electrónico válido."""
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(regex, email)

    def guardar_usuario(e):
        if (
            cedula_campo_texfield.value == ""
            or apellidos_campo_texfield.value == ""
            or nombres_campo_texfield.value == ""
            or mail_campo_texfield.value == ""
            or ciudad_campo_texfield.value == ""
        ):
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: Todos los campos deben estar llenos."),
                bgcolor=ft.colors.RED
            )
        elif len(cedula_campo_texfield.value) != 10:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: La cédula debe tener 10 dígitos."),
                bgcolor=ft.colors.RED
            )
        elif not validar_email(mail_campo_texfield.value):
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: Ingrese un correo electrónico válido."),
                bgcolor=ft.colors.RED
            )
        else:
            us.id.value = cedula_campo_texfield.value
            us.apellidos.value = apellidos_campo_texfield.value
            us.nombres.value = nombres_campo_texfield.value
            us.correo.value = mail_campo_texfield.value
            us.ciudad.value = ciudad_campo_texfield.value
            cedula_campo_texfield.value = ""
            apellidos_campo_texfield.value = ""
            nombres_campo_texfield.value = ""
            mail_campo_texfield.value = ""
            ciudad_campo_texfield.value = ""
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Cambio realizado con éxito!"),
                bgcolor=ft.colors.GREEN
            )
        page.snack_bar.open = True
        page.update()

    def limpiar_datos_usuario(e):
        cedula_campo_texfield.value = ""
        apellidos_campo_texfield.value = ""
        nombres_campo_texfield.value = ""
        mail_campo_texfield.value = ""
        ciudad_campo_texfield.value = ""
        page.update()
                   #!Alerta de reportar problema

    def close_Reporte_problemas(e):
        Reporte_problemas.open = False
        page.update()

    def Close_and_open_gracias(e):
        Reporte_problemas.open = False
        page.dialog = Mensaje_de_gracias
        Mensaje_de_gracias.open = True
        page.update()

    def close_dlg_mensaje_gracias(e):
        Mensaje_de_gracias.open = False
        page.update()

    Mensaje_de_gracias = ft.AlertDialog(
        modal=True,
        title=ft.Text("Muchas gracias por tu colaboración!",size=30),
        content=ft.Text("haremos lo posible para solucionarlo",size=15),
        actions=[
            ft.FilledButton("Volver al menu", on_click=close_dlg_mensaje_gracias),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.update()

    Reporte_problemas=ft.AlertDialog(
        modal=True,
        title=ft.Text("Reporte de problemas"),
        content=ft.Text("Por favor selecciona el problema junto a una descripción"),
        actions=[
            ft.Column(
                [
                    ft.Divider(),
                    ft.Checkbox(label="Problema de rendimiento", value=False),
                    ft.Checkbox(label="Error en mostrar datos", value=False),
                    ft.Checkbox(label="Error en el manejo de ventanas", value=False),
                    ft.Checkbox(label="Problemas de bugs", value=False),
                    ft.Checkbox(label="Calculos incorrectos", value=False),
                    ft.Checkbox(label="Otros...", value=False),
                    ft.TextField(
                        label="Describe el problema",
                        multiline=True,
                        max_length=250,
                        max_lines=5,
                    ),
                    ft.Row(
                        [
                            ft.FilledButton(
                                text="Volver",
                                on_click=close_Reporte_problemas,  
                            ),
                            ft.FilledButton(text="Enviar",
                                on_click=Close_and_open_gracias,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
            )
        ],
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    def open_dlg_modal_3(e):
        page.dialog = Reporte_problemas
        Reporte_problemas.open = True
        page.update()

    #!Alerta de cerrar secion
    def close_alert_cerrar_secion(e):
        Alert_cerrar_secion.open = False
        page.update()
    
    def close_alert_and_go_login(e):
        Alert_cerrar_secion.open = False
        page.go("/")
        page.update()

    Alert_cerrar_secion = ft.AlertDialog(
        modal=True,

        title=ft.Text("Por favor confirma"),
        content=ft.Text("Estas seguro de cerrar esta sesión?"),
        actions=[
            ft.TextButton("Si", on_click=close_alert_and_go_login),
            ft.TextButton("No", on_click=close_alert_cerrar_secion),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    
    def open_Alert_cerrar_secion(e):
        page.dialog = Alert_cerrar_secion
        Alert_cerrar_secion.open = True
        page.update()
    pages_configurar_usuario = ft.Column(
        [
            ft.Container(
                padding=0,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            height=60,
                            width=1365,
                            content=ft.Card(
                                elevation=1,
                                margin=5,
                                variant=ft.CardVariant.OUTLINED,
                                content=ft.Row(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            height=60,
                                            width=1200,
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                    ft.IconButton(
                                                        icon=ft.icons.ARROW_BACK,
                                                        on_click=regresar_al_home
                                                    ),
                                                    ft.Icon(name=ft.icons.MANAGE_ACCOUNTS_OUTLINED, size=40),
                                                    ft.VerticalDivider(),
                                                    ft.Text(
                                                        "Configurar usuario",
                                                        weight=ft.FontWeight.W_900,
                                                        color="#3d5ff5",
                                                        size=18
                                                    ),
                                                    ft.VerticalDivider()
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            height=60,
                                            width=1010,
                                            #border=ft.border.all(),
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                    ft.Row([
                                                        ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                        boton_dark_light_mode,
                                                        ft.PopupMenuButton(
                                                            items=[
                                                                ft.PopupMenuItem(),  # divider
                                                                ft.PopupMenuItem(
                                                                    content=ft.Row(
                                                                        [
                                                                            ft.Icon(ft.icons.BUG_REPORT),
                                                                            ft.Text("Reporte de errores"),
                                                                        ]
                                                                    ),
                                                                    on_click=open_dlg_modal_3
                                                                ),
                                                                ft.PopupMenuItem(),  # divider
                                                                ft.PopupMenuItem(
                                                                    content=ft.Row(
                                                                        [
                                                                            ft.Icon(ft.icons.EXIT_TO_APP),
                                                                            ft.Text("Cerrar la sesión"),
                                                                        ]
                                                                    ),
                                                                    on_click=open_Alert_cerrar_secion
                                                                ),
                                                                ft.PopupMenuItem(),  # divider
                                                            ]
                                                        )
                                                    ],alignment=ft.MainAxisAlignment.END)
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ),
                    ]
                )
            ),
            ft.Container(
                width=1365,
                height=650,
                content=ft.Row(
                    spacing=0,
                    controls=[
                        ft.Container(
                            width=1366,
                            height=650,
                            alignment=ft.alignment.top_center,
                            content=ft.Container(
                                width=800,
                                height=500,
                                padding=10,
                                alignment=ft.alignment.top_left,
                                content=ft.Card(
                                    elevation=10,
                                    variant=ft.CardVariant.OUTLINED,
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Row(
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        width=350,
                                                        height=500,
                                                        alignment=ft.alignment.center,
                                                        content=ft.Container(
                                                            alignment=ft.alignment.center,
                                                            height=500,
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Container(
                                                                        width=350,
                                                                        content=ft.Column(
                                                                            [
                                                                                ft.Divider(),
                                                                                ft.Text(
                                                                                    "    Configuración de Perfil:",
                                                                                    weight=ft.FontWeight.W_500,
                                                                                    size=25
                                                                                ),
                                                                                ft.Text("\n"),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(
                                                                        width=350,
                                                                        alignment=ft.alignment.center,
                                                                        content=ft.Row(
                                                                            [contenedor_imagen],
                                                                            alignment=ft.MainAxisAlignment.CENTER
                                                                        ),
                                                                    ),
                                                                    ft.Divider(
                                                                        color=ft.colors.TRANSPARENT
                                                                    ),
                                                                    ft.Container(
                                                                        width=350,
                                                                        content=ft.Row(
                                                                            [
                                                                                ft.OutlinedButton(
                                                                                    "Cambio de foto",
                                                                                    icon=ft.icons.ADD_A_PHOTO,
                                                                                    on_click=abrir_selector
                                                                                )
                                                                            ],
                                                                            alignment=ft.MainAxisAlignment.CENTER
                                                                        )
                                                                    ),
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    ft.Container(height=500, content=ft.VerticalDivider()),
                                                    ft.Container(
                                                        width=400,
                                                        height=500,
                                                        alignment=ft.alignment.center,
                                                        content=ft.Column(
                                                            [
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    padding=20,
                                                                    content=ft.Column(
                                                                        alignment=ft.VerticalAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Divider(height=90,color=ft.colors.TRANSPARENT),
                                                                            cedula_campo_texfield,
                                                                            ft.Row(
                                                                                [
                                                                                    nombres_campo_texfield,
                                                                                    apellidos_campo_texfield
                                                                                ]
                                                                            ),
                                                                            mail_campo_texfield,
                                                                            ciudad_campo_texfield,
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Row(
                                                                    [
                                                                        ft.ElevatedButton(
                                                                            "limpiar",
                                                                            bgcolor=ft.colors.RED,
                                                                            color=ft.colors.WHITE,
                                                                            on_click=limpiar_datos_usuario
                                                                        ),
                                                                        ft.ElevatedButton(
                                                                            "Guardar datos",
                                                                            on_click=guardar_usuario,
                                                                            bgcolor=ft.colors.GREEN,
                                                                            color=ft.colors.WHITE
                                                                        ),
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.END
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        ]
                                    )
                                )
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                )
            )
        ]
    )
    return ft.Row(
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        pages_configurar_usuario
                    ]
                )
            )
        ]
    )