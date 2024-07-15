import flet as ft

def view_consigurar_usuario(page: ft.Page):
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
                                    ft.Container(width=385,height=520
                                        ,border=ft.border.all()
                                    ),
                                    ft.Container(width=385,height=520
                                        ,border=ft.border.all()
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
    page.add(pages_configurar_usuario)

ft.app(target=view_consigurar_usuario)

