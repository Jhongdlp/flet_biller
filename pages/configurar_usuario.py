import flet as ft
import pages.home as us

def view_configurar_usuario(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=0


    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            boton_dark_light_mode.icon = ft.icons.DARK_MODE  # Icono de la luna
            #Contenedor_rail.bgcolor = '#202429'
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            boton_dark_light_mode.icon = ft.icons.LIGHT_MODE  # Icono de la luna
            #Contenedor_rail.bgcolor = '#f0f4fa'
        page.update()

    # Crear el botón de cambiar tema
    boton_dark_light_mode = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,  # Icono inicial del sol
        on_click=toggle_theme
    )
    def regresar_al_home(e):
        page.go("/home")
    
    imagen_actual = "https://concepto.de/wp-content/uploads/2018/10/usuario-e1539725586690.jpg" 

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
            contenedor_imagen.content.src = archivo.path  # Actualiza con la ruta del archivo
            page.update()

    selector_archivo = ft.FilePicker(on_result=seleccionar_imagen)
    page.overlay.append(selector_archivo)  # Agrega el FilePicker a la página

    def abrir_selector(e):
        selector_archivo.pick_files(
            allowed_extensions=["png", "jpg", "jpeg"],  # Filtra por extensiones
            dialog_title="Selecciona una imagen",
        )
    cedula_campo_texfield=ft.TextField(label="Ingresa tus cedula")    
    nombres_campo_texfield=ft.TextField(label="Ingresa tus nombres")
    apellidos_campo_texfield=ft.TextField(label="Ingresa tus apellidos")
    mail_campo_texfield=ft.TextField(label="Ingresa tu mail")
    ciudad_campo_texfield=ft.TextField(label="Ingresa tu ciudad")

    def guardar_usuario(e):
        us.id=cedula_campo_texfield.value
        us.apellidos=apellidos_campo_texfield.value
        us.nombres=nombres_campo_texfield.value
        
    pages_configurar_usuario=ft.Column([
        ft.Container(
            padding=0,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=60,width=1365,
                    #border=ft.border.all(color='#737780'),  
                    content=ft.Card(
                        elevation=1,
                        margin=5, 
                        variant=ft.CardVariant.OUTLINED,
                        content=ft.Row(spacing=0,controls=[
                            ft.Container(height=60,width=320,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    ft.IconButton(icon=ft.icons.ARROW_BACK,on_click=regresar_al_home),
                                    ft.Icon(name=ft.icons.GROUP_OUTLINED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Consifurar usuario",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    boton_dark_light_mode,
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=1366,height=650,
                    alignment=ft.alignment.center,
                    border=ft.border.all(),
                    content=ft.Container(
                        width=800,
                        height=550,
                        padding=10,
                        alignment=ft.alignment.top_left,
                        #border=ft.border.all(),
                        content=ft.Card(
                            elevation=10,
                            variant=ft.CardVariant.OUTLINED,
                            
                            content=ft.Column(spacing=0,controls=[
                                ft.Row(spacing=0,controls=[
                                    ft.Container(width=350,height=520,
                                        alignment=ft.alignment.center,
                                        #border=ft.border.all(),
                                        content=ft.Container(
                                            alignment=ft.alignment.center,
                                            #border=ft.border.all(),
                                            height=500,
                                            content=ft.Column(
                                                controls=
                                                [
                                                ft.Container(
                                                    width=350,
                                                    content=ft.Column([
                                                        ft.Divider(),
                                                        ft.Text("    Configuración de Perfil:",weight=ft.FontWeight.W_500,size=25),
                                                        ft.Text("\n"),
                                                    ])
                                                ),
                                                ft.Container(
                                                    width=350,
                                                    alignment=ft.alignment.center,
                                                    content= ft.Row([contenedor_imagen],alignment=ft.MainAxisAlignment.CENTER),
                                                ),
                                                ft.Divider(color=ft.colors.TRANSPARENT),
                                                ft.Container(width=350,content=ft.Row([
                                                    ft.OutlinedButton("Cambio de foto", icon=ft.icons.ADD_A_PHOTO ,on_click=abrir_selector)
                                                ],alignment=ft.MainAxisAlignment.CENTER)),
                                                
                                            ])
                                        )
                                    ),
                                    ft.Container(width=420,height=520
                                        ,border=ft.border.all(),
                                        content=ft.Column([
                                            cedula_campo_texfield,
                                            ft.Row([nombres_campo_texfield,apellidos_campo_texfield]),
                                            mail_campo_texfield,
                                            ciudad_campo_texfield,
                                            ft.ElevatedButton("Guardar datos",on_click=guardar_usuario)
                                        ])
                                        
                                    ),
                                ])
                            ])
                        )
                    )
                )
            ],alignment=ft.MainAxisAlignment.START)

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