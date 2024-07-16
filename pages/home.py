import flet as ft

id=ft.Text("")
apellidos=ft.Text("")
nombres=ft.Text("")
correo=ft.Text("")
ciudad=ft.Text("")

def HomePage(page: ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window_maximized=True
    page.title="Menu principal"
    page.window_title_bar_hidden = True
    page.padding=0
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
    def go_to_page_six(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/Inventario")
        page.update()
    def go_to_page_usuario(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        page.go("/config_usuario")
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
        Contenedor_Soporte_Ayuda.border = ft.border.all(3, border_color)
        Contenedor_configuraciones.border = ft.border.all(3, border_color)
        Contenedor_usuario.border = ft.border.all(3, border_color)
        page.update()
    #!==========================================PAGINA_UNO===========================================================
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
        on_click=go_to_page_two,
    )
    Contenedor_Soporte_Ayuda=ft.Container(
        content=ft.Container(width=230,height=180,
            content=ft.Column(spacing=0,controls=[
                ft.Container(width=230,height=70,
                    content=ft.Row([
                        ft.Icon(name=ft.icons.HELP_OUTLINE_OUTLINED,size=40)
                    ],alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(width=230,height=45,
                    content=ft.Row([ft.Text("Soporte y ayuda",weight=ft.FontWeight.W_900,size=20)
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(width=230,height=40,
                    content=ft.Row([ft.Text("Ver y solicitar ayuda o \nsoporte.",size=15)
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
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
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
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
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
                        ft.Container(height=60,width=500,
                            #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                            content=ft.Row([
                                ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                ft.TextField(
                                    height=35,
                                    #label="My favorite color",
                                    hint_text="Buscar",
                                    #helper_text="You can type only one color",
                                    #counter_text="0 symbols typed",
                                    prefix_icon=ft.icons.SEARCH_OUTLINED,
                                ),
                                boton_darl_ligth_mode
                            ])
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
                                                                src=f"src/perfil.png",
                                                                fit=ft.ImageFit.FILL,
                                                                repeat=ft.ImageRepeat.NO_REPEAT,
                                                            )
                                                        )
                                                        
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                    
                                                ),
                                                ft.Container(width=280,
                                                    content=ft.Row([
                                                        ft.Text("Jhon Andrade",weight=ft.FontWeight.W_900,size=20)
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
                                            Contenedor_Soporte_Ayuda,
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
