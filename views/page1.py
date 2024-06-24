import flet as ft
from flet_route import Params,Basket


def Page_1(page: ft.Page,params: Params, basket: Basket):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window_maximized=True
    page.window_title_bar_hidden = True
    page.padding=0

    def update_bgcolor():
        if page.theme_mode == ft.ThemeMode.DARK:
            rail.bgcolor = '#202429'
        else:
            rail.bgcolor = '#f0f4fa'
        page.update()

    rail = ft.NavigationRail(
        
        width=130,
        height=700,
        #bgcolor=ft.colors.AMBER,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        #extended=True,
        #bgcolor= ft.colors.GREEN_200,
        indicator_shape=ft.StadiumBorder(),
        elevation=20,
        #scale=1.03,
    
        #leading=(ft.Image("banner.png",width=100)),
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
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.ADD_ROUNDED),
                label_content=ft.Text("Configuraciones"),padding=13
            ),
        ],
        on_change=lambda e: change_index(e.control.selected_index),

    )
    def go_to_page_two(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        content.controls.pop()
        rail.selected_index = 1
        content.controls.append(page_two_ui)
        page.update()
    def go_to_page_three(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        content.controls.pop()
        rail.selected_index = 2
        content.controls.append(page_three_ui)
        page.update()
    def go_to_page_Four(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        content.controls.pop()
        rail.selected_index = 3
        content.controls.append(page_four_ui)
        page.update()
    def go_to_page_Five(e):
        # Elimina la página actual y agrega la interfaz de la página 2
        content.controls.pop()
        rail.selected_index = 4
        content.controls.append(page_five_ui)
        page.update()


    def minimizar_pagima(e):
        page.window_minimized=True
        page.update()

    def cerrar_login(end):
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Porfavor confirma"),
        content=ft.Text("Estas seguro de cerrar esta aplicacion?"),
        actions=[
            ft.ElevatedButton("Si", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            boton_darl_ligth_mode.icon = ft.icons.DARK_MODE  # Icono de la luna
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            boton_darl_ligth_mode.icon = ft.icons.LIGHT_MODE  # Icono del sol
        update_bgcolor()
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
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
    )
    
    page_one_ui=ft.Container(
        padding=0,
        content=ft.Column(spacing=0,controls=[
            ft.Container(height=25,width=1350,
                #border=ft.border.all(),
                content=ft.Row([
                    ft.IconButton(
                        icon=ft.icons.REMOVE_ROUNDED,
                        bgcolor=ft.colors.TRANSPARENT,
                        icon_size=15,
                        height=25,
                        on_click=minimizar_pagima
                    ),
                    ft.IconButton(
                        icon=ft.icons.CLEAR,
                        bgcolor=ft.colors.TRANSPARENT,
                        icon_size=15,
                        height=25,
                        on_click=cerrar_login
                    ),
                ],alignment=ft.MainAxisAlignment.END)
            ),
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
                                                        ft.Container(width=175,height=175,
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
                                                                ft.Text("ID:1750395012",size=15),
                                                                ft.Text("Apellidos: Andrade Guadalupe"),
                                                                ft.Text("Nombres: Jhon Paul"),
                                                                ft.Text("Correo: ejemplo@gmail.com"),
                                                                ft.Text("Ciudad: Quito"),
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
                                            ft.Container(ft.Text("Actividad reciente:",weight=ft.FontWeight.W_900,size=20)),
                                            ft.Container(width=280,height=133,
                                                #border=ft.border.all(),
                                                content=ft.Row(spacing=6,controls=[
                                                    ft.Container(width=87,height=100,
                                                        border=ft.border.all(),
                                                        border_radius=ft.border_radius.all(10),
                                                        padding=3,
                                                        shadow=ft.BoxShadow(
                                                            spread_radius=1,
                                                            blur_radius=5,
                                                            color=ft.colors.BLUE_GREY_300,
                                                            offset=ft.Offset(0, 0),
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                        ),
                                                        
                                                        
                                                        content=ft.Column([
                                                            ft.Text("Facturas\ngeneradas:",weight=ft.FontWeight.W_900,size=15),
                                                            ft.Text("12",weight=ft.FontWeight.W_900,size=25)
                                                        ])
                                                    ),
                                                    ft.Container(width=87,height=100,
                                                        border=ft.border.all(),
                                                        border_radius=ft.border_radius.all(10),
                                                        padding=3,
                                                        shadow=ft.BoxShadow(
                                                            spread_radius=1,
                                                            blur_radius=5,
                                                            color=ft.colors.BLUE_GREY_300,
                                                            offset=ft.Offset(0, 0),
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                        ),
                                                        content=ft.Column([
                                                            ft.Text("Clientes\nnuevos:",weight=ft.FontWeight.W_900,size=15),
                                                            ft.Text("5",weight=ft.FontWeight.W_900,size=25)
                                                        ])
                                                    ),
                                                    ft.Container(width=87,height=100,
                                                        border=ft.border.all(),
                                                        border_radius=ft.border_radius.all(10),
                                                        padding=3,
                                                        shadow=ft.BoxShadow(
                                                            spread_radius=1,
                                                            blur_radius=5,
                                                            color=ft.colors.BLUE_GREY_300,
                                                            offset=ft.Offset(0, 0),
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                        ),
                                                        content=ft.Column([
                                                            ft.Text("Cambios\ninventario:",weight=ft.FontWeight.W_900,size=15),
                                                            ft.Text("6",weight=ft.FontWeight.W_900,size=25)
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
                    ft.Container(width=1030,height=768,
                        #border=ft.border.all(),padding=20,
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
                            ft.Container(height=230,width=1000,
                                #border=ft.border.all(),
                                content=ft.Row([
                                    
                                    Contenedor_Dashboard,
                                    Contenedor_Soporte_Ayuda,
                                    Contenedor_usuario,
                                    Contenedor_configuraciones
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            )
                        ]), 
                    ),
                ],alignment=ft.MainAxisAlignment.START)
            ),   
        ])
    )
    page_two_ui=ft.Column([
        ft.Container(
            padding=0,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=25,width=1365,
                    #border=ft.border.all(),
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.icons.REMOVE_ROUNDED,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=minimizar_pagima
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLEAR,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=cerrar_login
                        ),
                    ],alignment=ft.MainAxisAlignment.END)
                ),
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
                                    ft.Icon(name=ft.icons.HISTORY_ROUNDED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Historial de facturas",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
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
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    #border=ft.border.all(),
                    content=ft.Row([rail])
                ) 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
    page_three_ui=ft.Column([
        ft.Container(
            padding=0,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=25,width=1365,
                    #border=ft.border.all(),
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.icons.REMOVE_ROUNDED,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=minimizar_pagima
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLEAR,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=cerrar_login
                        ),
                    ],alignment=ft.MainAxisAlignment.END)
                ),
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
                                    ft.Icon(name=ft.icons.LIBRARY_ADD_OUTLINED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Nueva factura",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
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
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    #border=ft.border.all(),
                    content=ft.Row([rail])
                ) 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
    page_four_ui=ft.Column([
        ft.Container(
            padding=0,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=25,width=1365,
                    #border=ft.border.all(),
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.icons.REMOVE_ROUNDED,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=minimizar_pagima
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLEAR,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=cerrar_login
                        ),
                    ],alignment=ft.MainAxisAlignment.END)
                ),
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
                                    ft.Icon(name=ft.icons.GROUP_OUTLINED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Clientes",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
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
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    #border=ft.border.all(),
                    content=ft.Row([rail])
                ) 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
    page_five_ui=ft.Column([
        ft.Container(
            padding=0,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=25,width=1365,
                    #border=ft.border.all(),
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.icons.REMOVE_ROUNDED,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=minimizar_pagima
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLEAR,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=cerrar_login
                        ),
                    ],alignment=ft.MainAxisAlignment.END)
                ),
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
                                    ft.Icon(name=ft.icons.INVENTORY_2_OUTLINED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Inventario",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
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
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    #border=ft.border.all(),
                    content=ft.Row([rail])
                ) 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
    pagina_six_ui=ft.Column([
        ft.Container(
            padding=0,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=25,width=1365,
                    #border=ft.border.all(),
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.icons.REMOVE_ROUNDED,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=minimizar_pagima
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLEAR,
                            bgcolor=ft.colors.TRANSPARENT,
                            icon_size=15,
                            height=25,
                            on_click=cerrar_login
                        ),
                    ],alignment=ft.MainAxisAlignment.END)
                ),
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
                                    ft.Icon(name=ft.icons.HISTORY_ROUNDED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Inventario",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
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
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    #border=ft.border.all(),
                    content=ft.Row([rail])
                ) 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )

    content = ft.Row([page_one_ui],vertical_alignment=ft.MainAxisAlignment.START)
    def change_index(e):
        index = e
        if index == 0:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 0
            content.controls.append(page_one_ui)
            page.update()

        if index == 1:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 1
            content.controls.append(page_two_ui)
            page.update()

        if index == 2:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 2
            content.controls.append(page_three_ui)
            page.update()
        if index == 3:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 3
            content.controls.append(page_four_ui)
            page.update()
        if index == 4:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 4
            content.controls.append(page_five_ui)
            page.update()
        if index == 5:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 4
            content.controls.append(pagina_six_ui)
            page.update()


    def on_keyboard(e: ft.KeyboardEvent):
        
        print(f"Key: {e.key}, Control: {e.ctrl}")
        if e.ctrl == True and e.key == "1":
            
            change_index(0)
            
        if e.ctrl == True and e.key == "2":
            
            change_index(1)

        if e.ctrl == True and e.key == "3":
            change_index(2)   
        page.update()
    page.on_keyboard_event = on_keyboard

    page.on_theme_mode_changed = lambda e: (update_bgcolor(), update_border_color())
    update_bgcolor()
    update_border_color()

    update_bgcolor()

    return ft.View(
        "/page1/:my_id",
        spacing=0,padding=0,
        controls=[
            content
        ]
    )