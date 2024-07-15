import flet as ft
from components.rail import create_navigation_rail
from datetime import datetime, timedelta
import pymysql
import itertools  

def view_estadistica_all(page: ft.Page):
    page.padding = 0

    Contenedor_rail = ft.Container(
        padding=0,
        width=140,
        height=650,
        content=ft.Card(
            variant=ft.CardVariant.OUTLINED,
            elevation=1,
            content=create_navigation_rail(page, selected_index=5),
        ),
    )

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
        on_click=toggle_theme,
    )

    # Conexión a la base de datos con pymysql
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="billify"
    )
    cursor = conexion.cursor()

    # Funciones para obtener datos (usando funciones de fecha de MySQL)
    def obtener_ventas_por_dia(dias):
        hoy = datetime.now().date()
        ventas_por_dia = []
        for i in range(dias):
            fecha = hoy - timedelta(days=i)
            cursor.execute(
                "SELECT SUM(REPLACE(SUBSTRING_INDEX(totales, ',', -1), ',', '')) FROM facturas WHERE DATE(fecha) = %s",
                (fecha,),
            )
            ventas = cursor.fetchone()[0] or 0
            ventas_por_dia.append((fecha.strftime("%d/%m"), ventas))
        return ventas_por_dia

    # ... [Otras funciones obtener_facturas_por_mes, etc. - comentadas por ahora] ...

    # Gráfico de ventas de los últimos 7 días
    ventas_7_dias = obtener_ventas_por_dia(7)
    grafico_ventas_dias = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=datos[0],
                bar_rods=[ft.BarChartRod(from_y=0, to_y=datos[1], width=20, color=ft.colors.BLUE_400)]
            )
            for datos in ventas_7_dias
        ],
        border=ft.border.all(color="#737780", width=1),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=500,
            color="#737780",
        ),
    )


    view_estadistica = ft.Column(
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
                                            width=320,
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                    ft.Icon(name=ft.icons.QUERY_STATS_ROUNDED, size=40),
                                                    ft.VerticalDivider(),
                                                    ft.Text("Estadistica", weight=ft.FontWeight.W_900,
                                                             color='#3d5ff5', size=18),
                                                    ft.VerticalDivider()
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            height=60,
                                            width=320,
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                    boton_dark_light_mode,
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

            # SOLO EL BARCHART DE VENTAS POR DÍA
            ft.Container(
                width=1365,
                height=650,
                content=ft.Row(
                    spacing=0,
                    controls=[
                        Contenedor_rail,
                        ft.Container(
                            width=1221,
                            height=650,
                            border=ft.border.all(),
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        content=grafico_ventas_dias,
                                        width=600,
                                        height=300,
                                    ),
                                ]
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START
                )
            ) 
        ]
    )
    page.add(view_estadistica)

ft.app(target=view_estadistica_all)