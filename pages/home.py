import flet as ft
import pages.login_page as lg
CORRECT_PASSWORD = "admin123"

id=ft.Text("")
apellidos=ft.Text("")
nombres=ft.Text("")
correo=ft.Text("")
ciudad=ft.Text("")

def HomePage(page: ft.Page):
    page.window_maximized=True
    page.title="Menu principal"
    page.window_title_bar_hidden = True
    page.padding=0
    page.favicon = "https://i.ibb.co/ZxS6FDs/Logo.png"
    page.update()
    def go_to_page_two(e):
        page.go("/Facturas")
        page.update()
    def go_to_page_three(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/generar_facturas")
        page.update()
    def go_to_page_Four(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/Clientes")
        page.update()
    def go_to_page_Five(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/Inventario")
        page.update()
    def go_to_page_config(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/Configuraciones")
        page.update()
    def go_to_page_usuario(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/config_usuario")
        page.update()
    def go_to_page_dashborad(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/Estadistica")
        page.update()
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            boton_darl_ligth_mode.icon = ft.icons.DARK_MODE  # Icono de la luna
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            boton_darl_ligth_mode.icon = ft.icons.DARK_MODE  # Icono de la luna
        update_border_color()          
        page.update()
        
    boton_darl_ligth_mode = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,  # Icono inicial del sol
        on_click=toggle_theme
    )
    def update_border_color():
        border_color = '#202429' if page.theme_mode == ft.ThemeMode.DARK else '#e4e5eb'
        Contenedor_inventario.border = ft.border.all(3, border_color)
        Contenedor_facturas.border = ft.border.all(3, border_color)
        Contenedor_clientes.border = ft.border.all(3, border_color)
        Contenedor_nueva_factura.border = ft.border.all(3, border_color)
        Contenedor_Dashboard.border = ft.border.all(3, border_color)
        Contenedor_agregar_productos.border = ft.border.all(3, border_color)
        Contenedor_configuraciones.border = ft.border.all(3, border_color)
        Contenedor_usuario.border = ft.border.all(3, border_color)
        page.update()
    #!==========================================PAGINA_UNO===========================================================
    
    def verify_password(e):
        if password_field.value == CORRECT_PASSWORD:
            print("Contraseña correcta")
            page.go("/Agregar_productos")
            page.dialog.open = False
            page.update()
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
    Contenedor_facturas=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.SHOPPING_CART_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Facturas",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y gestionar tus facturas\nemitidas.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_two,
    )
    Contenedor_nueva_factura=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.ADD_ROUNDED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Generar facturas",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y gestionar tus facturas\nemitidas.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_three,
    )
    Contenedor_clientes=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.GROUP_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Clientes",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y gestionar tus facturas\nemitidas.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_Four,
    )
    Contenedor_inventario=  ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.INVENTORY_2_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Inventario",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y gestionar tu inventario.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_Five,
    )

    Contenedor_Dashboard=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.QUERY_STATS_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Estadistica",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y gestionar tus\nestadisticas.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_dashborad,
    )
    Contenedor_agregar_productos=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.ADD_BUSINESS,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Agregar productos",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Agrega productos al inventario.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=open_dialog,
    )
    Contenedor_configuraciones=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.SETTINGS_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Configuraciones",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y configurar\nsistema.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_config,
    )
    Contenedor_usuario=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.MANAGE_ACCOUNTS_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Usuario",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y gestiona tu\n usuario.",size=15)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                ),
            ])
        ),
        #alignment=ft.alignment.center,
        margin=10,
        padding=10,
        alignment=ft.alignment.bottom_center,
        width=240,
        height=200,
        border_radius=10,
        ink=True,
        border=ft.border.all(3,color='#e4e5eb'),
        on_click=go_to_page_usuario,
    )

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
    
    
    usuario_text=ft.Text("",weight=ft.FontWeight.W_900,size=20)
    usuario_text.value=lg.Usuario.value
    page_one_ui=ft.Container(
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
                                ft.Icon(name=ft.icons.HOME_OUTLINED,size=40),
                                ft.VerticalDivider(),
                                ft.Text("Facturador electronico",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                #ft.Text("    "),
                                ft.VerticalDivider()
                            ])
                        ),
                        ft.Container(height=60,width=1010,
                            #border=ft.border.all(),
                            content=ft.Row([
                                ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                boton_darl_ligth_mode,
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
                        )
                    ]) 
                )          
            ),
            #!====================================================
            ft.Container(width=1365,
                content=ft.Row(spacing=0,controls=[
                    ft.Container(height=768,width=326,
                    #border=ft.border.all(),
                    content=ft.Card(elevation=1,show_border_on_foreground=False,variant=ft.CardVariant.OUTLINED,
                            content=ft.Container(width=326,height=768,
                                #border=ft.border.all(),
                                padding=15,
                                content=ft.Column(spacing=0,controls=[
                                    ft.Container(width=280,
                                        #border=ft.border.all(),
                                        border_radius=ft.border_radius.all(10),
                                        #bgcolor='#fdfcff',
                                        content=ft.Card(elevation=3,
                                            content=ft.Column([
                                                ft.Divider(),
                                                ft.Container(
                                                    content=ft.Row([
                                                        ft.Container(width=175,height=147,
                                                            #border=ft.border.all(),
                                                            border_radius=ft.border_radius.all(100),
                                                            padding=0,
                                                            content=ft.Image(
                                                                #opacity=0.5,
                                                                src=f"https://i.ibb.co/k8WKhZw/perfil.png",
                                                                fit=ft.ImageFit.FILL,
                                                                repeat=ft.ImageRepeat.NO_REPEAT,
                                                            )
                                                        )
                                                        
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                    
                                                ),
                                                ft.Container(width=280,
                                                    content=ft.Row([
                                                        usuario_text,
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                ),
                                                ft.Container(width=280,
                                                    content=ft.Row([
                                                        ft.Container(
                                                            #border=ft.border.all(),
                                                            content=ft.Column([
                                                                ft.Row([ft.Text("ID:",size=15),id]),
                                                                ft.Row([ft.Text("Apellidos:"),apellidos]),
                                                                ft.Row([ft.Text("Nombres:"),nombres]),
                                                                ft.Row([ft.Text("Correo:"),correo]),
                                                                ft.Row([ft.Text("Ciudad:"),ciudad])
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            ])             
                                                        )
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                ),
                                                ft.Divider()
                                            ])
                                        )
                                    ),
                                    ft.Container(
                                        #border=ft.border.all(),
                                        content=ft.Column([
                                            ft.Container(ft.Text("Actividad reciente:",weight=ft.FontWeight.W_900,size=17)),
                                            ft.Container(width=280,height=80,
                                                #border=ft.border.all(),
                                                content=ft.Row(spacing=6,controls=[
                                                    ft.Container(width=87,height=75,
                                                        border=ft.border.all(color='#97999b'),
                                                        border_radius=ft.border_radius.all(10),
                                                        padding=5,
                                                        content=ft.Column(spacing=3,controls=[
                                                            ft.Text("Facturas\ngeneradas:",weight=ft.FontWeight.W_900,size=12),
                                                            ft.Text("12",weight=ft.FontWeight.W_900,size=20)
                                                        ])
                                                    ),
                                                    ft.Container(width=87,height=75,
                                                        border=ft.border.all(color='#97999b'),
                                                        border_radius=ft.border_radius.all(10),
                                                        padding=5,  
                                                        content=ft.Column(spacing=3,controls=[
                                                            ft.Text("Clientes\nnuevos:",weight=ft.FontWeight.W_900,size=12),
                                                            ft.Text("5",weight=ft.FontWeight.W_900,size=20)
                                                        ])
                                                    ),
                                                    ft.Container(width=87,height=75,
                                                        border=ft.border.all(color='#97999b'),
                                                        border_radius=ft.border_radius.all(10),
                                                        padding=5, 
                                                        content=ft.Column(spacing=3,controls=[
                                                            ft.Text("Cambios\ninventario:",weight=ft.FontWeight.W_900,size=12),
                                                            ft.Text("6",weight=ft.FontWeight.W_900,size=20)
                                                        ])
                                                    )
                                                ],alignment=ft.MainAxisAlignment.CENTER)         
                                            )
                                        ])
                                    )
                                ])
                            ),
                        )
                    ),
                    ft.Column(spacing=0,controls=[
                        ft.Container(width=1030,height=768,
                            #border=ft.border.all(),
                            content=
                                ft.Container(width=1030,
                                    content=ft.Column([
                                    ft.Container(height=300,width=1000,
                                        #border=ft.border.all(),
                                        content=ft.Row([
                                            Contenedor_facturas,Contenedor_nueva_factura,Contenedor_clientes,
                                            Contenedor_inventario
                                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                                    ),
                                    #!===============================================
                                    #!===============================================
                                    ft.Container(height=200,width=1000,
                                        #border=ft.border.all(),
                                        content=ft.Row([
                                            
                                            Contenedor_Dashboard,
                                            Contenedor_agregar_productos,
                                            Contenedor_usuario,
                                            Contenedor_configuraciones
                                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                                    )
                                ]), 
                            )
                        ),
                    ]),      
                ],alignment=ft.MainAxisAlignment.START)
            ),   
        ])
    )
    return ft.Row(
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        page_one_ui
                    ]
                )
            )
        ]
    )
