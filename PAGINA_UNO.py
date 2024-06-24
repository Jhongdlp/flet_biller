import flet as ft
import bd.base_implemtnacion as bd

def main(page: ft.Page):
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
    #!==================================================================================
    #!=                                                                                =
    #!=                                 PAGINA DOS                                     =
    #!=                                                                                =
    #!==================================================================================    
    page_two_ui=ft.Column([
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
        ft.Container(width=1366,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    border=ft.border.all(),
                    content=ft.Row([rail])
                ),
                ft.Container(width=1221,height=650,
                    border=ft.border.all()             
                ), 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
     #!==================================================================================
    #!=                                                                                =
    #!=                                 PAGINA TRES                                     =
    #!=                                                                                =
    #!==================================================================================    
    subtotal_value = ft.Text(value="0.00")
    iva_value = ft.Text(value="0.00")
    total_value = ft.Text(value="0.00")
    
    card_totales_generar=ft.Card(elevation=5,content=ft.Container(
        width=170,
        height=135,
        padding=10,
        content=ft.Column(spacing=0,controls=[
            ft.Row([ft.Text("Subtotal: "), subtotal_value]),
            ft.Row([ft.Text("Iva: "), iva_value]),
            ft.Row([ft.Text("Total: "), total_value]),
            ft.Divider(color=ft.colors.TRANSPARENT),
            ft.ElevatedButton("Generar Factura",
            width=160,
            height=35,
            bgcolor=ft.colors.INDIGO_600,
            color=ft.colors.WHITE,
            #on_click=open_dlg_generar_factura
            ),
            ft.Divider(color=ft.colors.TRANSPARENT),
        ])
    ))


    id_producto = ft.TextField(width=150,height=30,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        content_padding=5                          
    )

    data_table = ft.DataTable(
        width=800,
        column_spacing=15,
        columns=[
            ft.DataColumn(ft.Text("No."), tooltip="Número de fila"),
            ft.DataColumn(ft.Text("ID"), tooltip="ID del Producto"),
            ft.DataColumn(ft.Text("Nombre"), tooltip="Nombre del Producto"),
            ft.DataColumn(ft.Text("Tipo"), tooltip="Tipo del Producto"),
            ft.DataColumn(ft.Text("Iva"), tooltip="IVA del Producto"),
            ft.DataColumn(ft.Text("Precio"), tooltip="Precio del Producto"),
            ft.DataColumn(ft.Text("Cantidad"), tooltip="Cantidad"),
            ft.DataColumn(ft.Text("Acción"), tooltip="Acciones disponibles")
        ],
        rows=[],
    )

    scrollable_container = ft.Container(
        height=300,
        content=ft.Column([data_table], scroll=ft.ScrollMode.AUTO)
    )

    def update_row_numbers():
        for i, row in enumerate(data_table.rows):
            row.cells[0] = ft.DataCell(ft.Text(str(i + 1)))

    def calculate_subtotal():
        subtotal = 0.0
        for row in data_table.rows:
            cantidad_str = row.cells[6].content.value
            cantidad = int(cantidad_str) if cantidad_str.isdigit() else 0
            precio = float(row.cells[5].content.value)
            subtotal += cantidad * precio
        subtotal_value.value = f"{subtotal:.2f}"
        iva = subtotal * 0.12
        iva_value.value = f"{iva:.2f}"
        total_value.value = f"{subtotal + iva:.2f}"
        page.update()

    def add_product(e):
        product_id = id_producto.value
        if not product_id.isdigit():
            print("Error: El ID del producto debe ser mayor a 0.")
            id_producto.focus()
            return

        product_data = bd.get_product_data(product_id)

        if not product_data:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: El producto con ID {product_id} no se encontró en la base de datos.",
                size=20),
                bgcolor=ft.colors.RED_400,
                duration=2000,
            )
            page.snack_bar.open = True
            id_producto.focus()
            page.update()
            return

        for row in data_table.rows:
            if row.cells[1].content.value == product_data[0]:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"El producto con ID {product_data[0]} ya ha sido  agregado.",size=20,color=ft.colors.WHITE),
                    bgcolor=ft.colors.BLUE_800,
                    duration=2000,
                    show_close_icon=True,
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

        cantidad_producto = ft.TextField(value="1", width=50,height=40,
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
            max_length=4,
            content_padding=2,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.colors.TRANSPARENT,
            filled=True,                                  
        )

        def validate_cantidad(e):
            if not cantidad_producto.value.isdigit():
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser un número."),duration=2000,
                )
                page.snack_bar.open = True
                page.update()
                return

            cantidad = int(cantidad_producto.value)
            existencias = product_data[5]

            if cantidad <= 0:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser mayor que cero."),duration=2000,                       
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

            if cantidad > existencias:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad ingresada {cantidad} excede las existencias disponibles {existencias} para el producto {product_data[1]} (ID: {product_data[0]})."),
                    duration=2000,
                )
                page.snack_bar.open = True
                page.update()
                return

            calculate_subtotal()

        cantidad_producto.on_change = validate_cantidad

        new_row = ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(len(data_table.rows) + 1))),
            ft.DataCell(ft.Text(product_data[0])),
            ft.DataCell(ft.Text(product_data[1])),
            ft.DataCell(ft.Text(product_data[2])),
            ft.DataCell(ft.Text(product_data[3])),
            ft.DataCell(ft.Text(product_data[4])),
            ft.DataCell(cantidad_producto),
            ft.DataCell(ft.IconButton(
                icon=ft.icons.DELETE_FOREVER,
                tooltip="Eliminar producto",
                on_click=lambda e: delete_product(e, new_row)
            ))
        ])
        data_table.rows.append(new_row)
        id_producto.value = ""
        id_producto.focus()  # Establece el foco en el TextField después de agregar el producto
        page.update()
        calculate_subtotal()

    def delete_product(e, row):
        data_table.rows.remove(row)
        update_row_numbers()
        page.update()
        calculate_subtotal()

    def delete_all_rows(e):
        data_table.rows.clear()
        update_row_numbers()
        page.update()
        calculate_subtotal()

    id_producto.on_submit = add_product

    delete_all_button = ft.ElevatedButton(text="Eliminar todas las filas", on_click=delete_all_rows)

    Boton_consumirdor_final=ft.ElevatedButton("Consumidor final",width=158,height=35,bgcolor=ft.colors.GREEN_500,color="WHITE",
        #on_click=Boton_Consumidor_final_logica
        )
    Boton_Eliminar_Datos=ft.ElevatedButton("Eliminar Datos",width=147,height=35,bgcolor=ft.colors.RED,color=ft.colors.WHITE,
        #on_click=Boton_Eliminar_Datos_logica
        )
    page_three_ui=ft.Column([
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
                ),
                ft.Container(width=1221,height=650,
                    #border=ft.border.all(),
                    content=ft.Column(spacing=0,controls=[
                        ft.Row(spacing=0,controls=[
                            ft.Container(width=500,height=600,
                                #border=ft.border.all(),
                                content=ft.Column(spacing=0,controls=[
                                    ft.Text("Datos de cliente",size=25),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("Cedula"),width=230,height=35.),
                                        ft.IconButton(icon=ft.icons.DOCUMENT_SCANNER),
                                        ft.IconButton(icon=ft.icons.DOCK)
                                    ]),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("Nombre"),width=230,height=35),
                                        ft.VerticalDivider(),
                                        ft.TextField(label=("Apellido"),width=230,height=35),
                                    ]),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("Direccion"),width=230,height=35),
                                        ft.VerticalDivider(),
                                        ft.TextField(label=("Telefono"),width=230,height=35),
                                    ]),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("E-Mail"),width=475,height=35),
                                        
                                    ]),
                                    ft.Divider(),
                                    ft.Row([
                                        Boton_Eliminar_Datos,
                                        Boton_consumirdor_final,
                                        card_totales_generar,
                                    ])
            
                                    
                                ])
                            ),
                            ft.Container(height=600,content=(
                                ft.Row([ft.VerticalDivider(),])
                            )),
                            ft.Container(width=700,height=600   ,
                                #border=ft.border.all(),
                                content=ft.Column(spacing=0,
                                    controls=[
                                        ft.Row([ft.Text("Ingresa el ID de los productos",size=25),id_producto,delete_all_button]),ft.Divider(), scrollable_container, 
                                ])
                            ),
                        ])
                    ])             
                ), 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
    page_four_ui=ft.Column([
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
    page.add(content)

ft.app(target=main)