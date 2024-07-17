import flet as ft
from components.rail import create_navigation_rail

class State:
    toggle = True

s = State()

def view_estadistica_all(page: ft.Page):
    page.title="Estadistica"
    page.padding=0

    Contenedor_rail =ft.Container(padding=0,
        width=140,
        height=650,
        content=ft.Card(
                #margin=5,
                variant=ft.CardVariant.OUTLINED,
                elevation=1,
                content=create_navigation_rail(page, selected_index=5)
            )
    
    ) 
    
    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 1.5),
                ft.LineChartDataPoint(5, 1.4),
                ft.LineChartDataPoint(7, 3.4),
                ft.LineChartDataPoint(10, 2),
                ft.LineChartDataPoint(12, 2.2),
                ft.LineChartDataPoint(13, 1.8),
            ],
            stroke_width=8,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 2.8),
                ft.LineChartDataPoint(7, 1.2),
                ft.LineChartDataPoint(10, 2.8),
                ft.LineChartDataPoint(12, 2.6),
                ft.LineChartDataPoint(13, 3.9),
            ],
            color=ft.colors.PINK,
            below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 2.8),
                ft.LineChartDataPoint(3, 1.9),
                ft.LineChartDataPoint(6, 3),
                ft.LineChartDataPoint(10, 1.3),
                ft.LineChartDataPoint(13, 2.5),
            ],
            color=ft.colors.CYAN,
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
    ]

    data_2 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 4),
                ft.LineChartDataPoint(5, 1.8),
                ft.LineChartDataPoint(7, 5),
                ft.LineChartDataPoint(10, 2),
                ft.LineChartDataPoint(12, 2.2),
                ft.LineChartDataPoint(13, 1.8),
            ],
            stroke_width=4,
            color=ft.colors.with_opacity(0.5, ft.colors.LIGHT_GREEN),
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 2.8),
                ft.LineChartDataPoint(7, 1.2),
                ft.LineChartDataPoint(10, 2.8),
                ft.LineChartDataPoint(12, 2.6),
                ft.LineChartDataPoint(13, 3.9),
            ],
            color=ft.colors.with_opacity(0.5, ft.colors.PINK),
            below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.PINK),
            stroke_width=4,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 3.8),
                ft.LineChartDataPoint(3, 1.9),
                ft.LineChartDataPoint(6, 5),
                ft.LineChartDataPoint(10, 3.3),
                ft.LineChartDataPoint(13, 4.5),
            ],
            color=ft.colors.with_opacity(0.5, ft.colors.CYAN),
            stroke_width=4,
            stroke_cap_round=True,
        ),
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4,
                    label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        ft.Text(
                            "OCT",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "DEC",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=4,
        min_x=0,
        max_x=14,
        # animate=5000,
        expand=True,
    )

    def toggle_data(e):
        if s.toggle:
            chart.data_series = data_2
            chart.data_series[2].point = True
            chart.max_y = 6
            chart.interactive = False
        else:
            chart.data_series = data_1
            chart.max_y = 4
            chart.interactive = True
        s.toggle = not s.toggle
        chart.update()

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
    view_estadistica=ft.Column([
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
                            ft.Container(height=60,width=1200,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    ft.Icon(name=ft.icons.QUERY_STATS_ROUNDED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Estadistica",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=1010,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                content=ft.Row([
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
                ft.Container(width=1221,height=650
                    ,content=ft.Row([ft.IconButton(ft.icons.REFRESH, on_click=toggle_data), chart])
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
                        view_estadistica
                    ]
                )
            )
        ]
    )

