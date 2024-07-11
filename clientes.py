import flet as ft
from components.rail import create_navigation_rail

def main(page: ft.page):

    Contenedor_rail =ft.Container(padding=0,
        width=140,
        height=650,
        content=ft.Card(
                #margin=5,
                variant=ft.CardVariant.OUTLINED,
                elevation=1,
                content=create_navigation_rail(page, selected_index=3)
            )
    
    ) 

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
    cedula_campo_texfild=ft.TextField(hint_text="Cedula",
        content_padding=5,
        width=175,  
        height=35,           
    )
    nombre_cliente_texfield=ft.TextField(hint_text="Nombre del cliente",
        content_padding=5,
        width=175,  
        height=35,           
    )   
    apellido_cliente_texfield=ft.TextField(hint_text="Apellido del cliente",
        content_padding=5,
        width=175,
        height=35
    )
    direccion_cliente_texfield=ft.TextField(hint_text="Direccion",
        content_padding=5,
        min_lines=4, # Controla la altura visible
        max_lines=4,
        #height=100, # Define la altura fija
        width=360,
        max_length=150,  
        #height=35,           
    )
    telefono_cliente_texfield=ft.TextField(hint_text="Telefono del cliente",
        content_padding=5,
        width=115,  
        height=35,     
    )
    mail_cliente_texfield=ft.TextField(hint_text="Mail del cliente",
        content_padding=5,
        width=240,
        height=35
    )
    view_clientes=ft.Column([
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
                Contenedor_rail,
                ft.Container(width=1200,height=650,
                    #border=ft.border.all(),
                    alignment=ft.alignment.top_left,
                    content=ft.Row(spacing=0,controls=[
                        ft.Container(width=400,height=600,
                            #border=ft.border.all(),
                            #padding=5,
                            alignment=ft.alignment.center,
                            content=ft.Container(width=395,height=595,
                                #border=ft.border.all(),
                                content=ft.Card(elevation=10,
                                    content=ft.Column([
                                        ft.Container(width=395,
                                            alignment=ft.alignment.center,
                                            padding=10,
                                            content=ft.Column([
                                                ft.Text("    Agregar Cliente",weight=ft.FontWeight.W_900,size=25),
                                                ft.Text("Ingrese los datos de un nuevo cliente",size=15)
                                            ])
                                        ),
                                        ft.Divider(),
                                        ft.Container(width=395,
                                            alignment=ft.alignment.center,
                                            padding=10,
                                            content=ft.Column([
                                                ft.Container(
                                                    alignment=ft.alignment.center_left,
                                                    content=ft.Row([
                                                        ft.Column([
                                                            ft.Text("Identificador:",weight=ft.FontWeight.W_900,size=14),
                                                            ft.Row([
                                                                cedula_campo_texfild,
                                                                ft.IconButton(icon=ft.icons.DOCUMENT_SCANNER_ROUNDED),
                                                                ft.IconButton(icon=ft.icons.FEATURED_VIDEO_OUTLINED),
                                                            ]),         
                                                            
                                                        ]),
                                                ]),
                                                ),
                                                ft.Row([
                                                    ft.Column([
                                                        ft.Text("Nombre:",weight=ft.FontWeight.W_900,size=14),
                                                        nombre_cliente_texfield
                                                        
                                                    ]),
                                                    ft.Column([
                                                        ft.Text("Apellido:",weight=ft.FontWeight.W_900,size=14),
                                                        apellido_cliente_texfield
                                                    ]),

                                                ]),
                                                ft.Column([
                                                    ft.Text("Direccion:",weight=ft.FontWeight.W_900,size=14),
                                                    direccion_cliente_texfield
                                                    
                                                ]),
                                                ft.Row([
                                                    ft.Column([
                                                        ft.Text("Telefono:",weight=ft.FontWeight.W_900,size=14),
                                                        telefono_cliente_texfield
                                                        
                                                    ]),
                                                    ft.Column([
                                                        ft.Text("mail:",weight=ft.FontWeight.W_900,size=14),
                                                        mail_cliente_texfield
                                                    ])
                                                ]),
                                                ft.Divider(height=3),
                                                ft.Container(
                                                    alignment=ft.alignment.top_right,
                                                    content=ft.Row([
                                                        ft.ElevatedButton("Limpiar",bgcolor=ft.colors.RED_600,color=ft.colors.WHITE),
                                                        ft.ElevatedButton("Guardar cliente",bgcolor=ft.colors.GREEN_600,color=ft.colors.WHITE), 
                                                    ],ft.MainAxisAlignment.END)
                                                )
                                                
                                            ])            
                                        ),
                                    ])
                                )                 
                            )
                        ),
                        ft.Container(width=800,height=600,
                            #border=ft.border.all(),
                            alignment=ft.alignment.center,
                            content=ft.Column([
                                ft.Container(width=795,
                                    #height=50,
                                    border=ft.border.all(),
                                    padding=10,
                                    content=ft.Container(
                                        ft.Column([
                                            ft.Text("Busca a un cliente:",weight=ft.FontWeight.W_900,size=25),
                                            ft.Row([
                                                ft.TextField(label="Bucar por cedula",width=250),
                                                ft.TextField(label="Bucar por RUC",width=250),
                                                ft.TextField(label="Bucar por pasaporte",width=250),
                                            ])
                                        ]),
                                        
                                    )                 
                                ),
                                ft.Container(width=795
                                    #!PONER AQUI EL DATATABLE DE LA GENERACION DE LA BUSQUEDA
                                )
                            ])
                        ),
                    ])

                )
            ],alignment=ft.MainAxisAlignment.START)
        )
        ]
    )
    page.add(view_clientes)
ft.app(main)