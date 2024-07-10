import flet as ft
from components.rail import create_navigation_rail

def main(page: ft.page):
    pagina=ft.Text("Funciona")
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
                                                ft.Row([
                                                    ft.Column([
                                                        ft.Text("Nombre:",weight=ft.FontWeight.W_900,size=14),
                                                        ft.TextField(hint_text="Nombre del cliente",
                                                            content_padding=5,
                                                            width=175,  
                                                            height=35,           
                                                        )
                                                        
                                                    ]),
                                                    ft.Column([
                                                        ft.Text("Apellido:",weight=ft.FontWeight.W_900,size=14),
                                                        
                                                        ft.TextField(hint_text="Apellido del cliente",
                                                            content_padding=5,
                                                            width=175,
                                                            height=35
                                                        )
                                                    ]),

                                                ]),
                                                ft.Column([
                                                    ft.Text("Direccion:",weight=ft.FontWeight.W_900,size=14),
                                                    ft.TextField(hint_text="Direccion",
                                                        content_padding=5,
                                                        width=175,  
                                                        height=35,           
                                                    )
                                                    
                                                ]),
                                                ft.Row([
                                                    ft.Column([
                                                        ft.Text("Telefono:",weight=ft.FontWeight.W_900,size=14),
                                                        ft.TextField(hint_text="Telefono del cliente",
                                                            content_padding=5,
                                                            width=115,  
                                                            height=35,     
                                                        )
                                                        
                                                    ]),
                                                    ft.Column([
                                                        ft.Text("mail:",weight=ft.FontWeight.W_900,size=14),
                                                        
                                                        ft.TextField(hint_text="Mail del cliente",
                                                            content_padding=5,
                                                            width=240,
                                                            height=35
                                                        )
                                                    ])
                                                ]),
                                                
                                            ])            
                                        ),
                                    ])
                                )                 
                            )
                        ),
                        ft.Container(width=800,height=600,
                            #border=ft.border.all(),
                            alignment=ft.alignment.center,
                            content=ft.Container(width=795,height=595,
                                #border=ft.border.all(),
                                padding=10,
                                content=ft.Container(ft.Text("ola"))                 
                            )
                        ),
                    ])

                )
            ],alignment=ft.MainAxisAlignment.START)

        )
        ]
    )
    page.add(view_clientes)
ft.app(main)