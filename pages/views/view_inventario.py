import flet as ft
from components.rail import create_navigation_rail
import pymysql
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="billify"
    )

# Consulta para obtener el número total de registros
def get_total_records():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos")
    total_records = cursor.fetchone()[0]
    db.close()
    return total_records

# Parámetros de paginación
page_size = 10
total_records = get_total_records()
total_pages = (total_records + page_size - 1) // page_size  # Redondeo hacia arriba

# Variable para almacenar la página actual
current_page_label = ft.Text(value="Página 1 de {}".format(total_pages))

# Función para obtener datos de una página específica con filtros de búsqueda
def get_page(page, search_query='', search_tip_prod='', search_tip_esp_prod=''):
    offset = (page - 1) * page_size
    db = get_db_connection()
    cursor = db.cursor()
    
    query = "SELECT ID_PROD, NOM_PROD, TIP_PROD, TIP_ESP_PROD, MAR_PRO, IVA_PRO, PRE_PRO, EXIS_PRO FROM productos WHERE 1"
    params = []
    
    if search_query:
        query += " AND NOM_PROD LIKE %s"
        params.append('%' + search_query + '%')
    if search_tip_prod:
        query += " AND TIP_PROD = %s"
        params.append(search_tip_prod)
    if search_tip_esp_prod:
        query += " AND TIP_ESP_PROD = %s"
        params.append(search_tip_esp_prod)
    
    query += f" LIMIT {page_size} OFFSET {offset}"
    
    cursor.execute(query, params)
    data = cursor.fetchall()
    if len(data) == 0:
        print("Error: No se encontraron resultados para la búsqueda.")
    
    # Obtener el número total de registros después de aplicar los filtros
    cursor.execute(f"SELECT COUNT(*) FROM productos WHERE 1 {'AND NOM_PROD LIKE %s' if search_query else ''} {'AND TIP_PROD = %s' if search_tip_prod else ''} {'AND TIP_ESP_PROD = %s' if search_tip_esp_prod else ''}", params)
    total_records_filtered = cursor.fetchone()[0]
    global total_pages
    total_pages = (total_records_filtered + page_size - 1) // page_size  # Redondeo hacia arriba
    
    db.close()
    return data, total_records_filtered

# Función para actualizar los datos en la tabla
def update_page(page, page_number, search_query='', search_tip_prod='', search_tip_esp_prod=''):
    data, total_records_filtered = get_page(page_number, search_query, search_tip_prod, search_tip_esp_prod)
    data_table.rows.clear()
    for row in data:
        data_table.rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(cell)) for cell in row
        ]))
    current_page_label.value = "Página {} de {}".format(page_number, total_pages)
    page.update()
    update_pagination_controls(page, page_number, total_records_filtered)

# Función para actualizar los controles de paginación
def update_pagination_controls(page, current_page=1, total_records_filtered=None):
    pagination_controls.controls.clear()

    if current_page > 1:
        pagination_controls.controls.append(
            ft.IconButton( icon=ft.icons.KEYBOARD_DOUBLE_ARROW_UP_OUTLINED, width=55,on_click=lambda e: update_page(page, 1, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
        pagination_controls.controls.append(
            ft.IconButton( icon=ft.icons.KEYBOARD_ARROW_UP_OUTLINED, width=55,on_click=lambda e: update_page(page, current_page - 1, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )

    for i in range(max(1, current_page - 2), min(total_pages + 1, current_page + 3)):
        pagination_controls.controls.append(
            ft.TextButton(text=str(i), on_click=lambda e, p=i: update_page(page, p, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
    
    if current_page < total_pages:
        pagination_controls.controls.append(
            ft.IconButton( icon=ft.icons.KEYBOARD_ARROW_DOWN_OUTLINED, width=55,on_click=lambda e: update_page(page, current_page + 1, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
        pagination_controls.controls.append(
            ft.IconButton( icon=ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN_ROUNDED, width=55,on_click=lambda e: update_page(page, total_pages, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
    
    page.update()

# Función de búsqueda
def search_product(event, page):
    search_query = search_field.value
    search_tip_prod = search_tip_prod_field.value
    search_tip_esp_prod = search_tip_esp_prod_field.value
    
    # Si todos los campos de búsqueda están vacíos, restablecer al estado original
    if not search_query and not search_tip_prod and not search_tip_esp_prod:
        update_page(page, 1)
    else:
        update_page(page, 1, search_query, search_tip_prod, search_tip_esp_prod)

# Función para limpiar los campos de búsqueda y restablecer la tabla
def clear_search_fields(event, page):
    search_field.value = ""
    search_tip_prod_field.value = ""
    search_tip_esp_prod_field.value = ""
    search_product(event, page)

def view_inventario_all(page: ft.Page):
    #page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=0
    global data_table, search_field, search_tip_prod_field, search_tip_esp_prod_field, pagination_controls
    page.title = "Inventario"

    data_table = ft.DataTable(
        width=1100,
        scale=0.99,
        columns=[
            ft.DataColumn(ft.Text("ID_PROD")),
            ft.DataColumn(ft.Text("NOM_PROD")),
            ft.DataColumn(ft.Text("TIP_PROD")),
            ft.DataColumn(ft.Text("TIP_ESP_PROD")),
            ft.DataColumn(ft.Text("MAR_PRO")),
            ft.DataColumn(ft.Text("IVA_PRO")),
            ft.DataColumn(ft.Text("PRE_PRO")),
            ft.DataColumn(ft.Text("EXIS_PRO")),
        ],
        rows=[]
    )

    # Campos de búsqueda
    search_field = ft.TextField(
        label="Buscar por Nombre",
        width=200,
        height=40,
        content_padding=5,
        on_submit=lambda event: search_product(event, page)
    )
    
    search_tip_prod_field = ft.TextField(
        label="Buscar por Tipo de Producto",
        width=200,
        height=40,
        content_padding=5, 
        on_submit=lambda event: search_product(event, page)
    )
    
    search_tip_esp_prod_field = ft.TextField(
        label="Buscar por Tipo Específico de Producto",
        width=200,
        height=40,
        content_padding=5,
        on_submit=lambda event: search_product(event, page)
    )

    # Botón para limpiar los campos de búsqueda
    clear_button = ft.TextButton(
        text="Limpiar",
        on_click=lambda event: clear_search_fields(event, page)
    )

    # Controles de paginación
    pagination_controls = ft.Column([])
    update_pagination_controls(page)

    Contenedor_rail =ft.Container(padding=0,
        width=140,
        height=650,
        content=ft.Card(
                #margin=5,
                variant=ft.CardVariant.OUTLINED,
                elevation=1,
                content=create_navigation_rail(page, selected_index=4)
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
    view_inventario=ft.Column([
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
                            ft.Container(height=60,width=380,
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
                            ft.Container(height=60,width=1100,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                alignment=ft.alignment.top_left,
                                padding=0,
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    search_field,
                                    search_tip_prod_field,
                                    search_tip_esp_prod_field,
                                    clear_button,
                                    current_page_label,  # Indicador de la página actual,
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
                ft.Container(width=1221,height=650,
                    #border=ft.border.all(),
                    alignment=ft.alignment.top_center,
                    content=ft.Container(width=1221,height=528,
                        alignment=ft.alignment.top_center,
                        content=ft.Row([
                            ft.Container(
                                width=1100,
                                padding=0,
                                #height=500,
                                alignment=ft.alignment.top_center,
                                #border=ft.border.all(),
                                content=(ft.Row(spacing=0,controls=[data_table]))  # Mostrar la primera página inicialment)
                            ),
                            #update_page(page, 1),
                            ft.Container(
                                width=100,
                                padding=0,
                                height=528,
                                #border=ft.border.all(),
                                alignment=ft.alignment.center,
                                content=(ft.Card(
                                    elevation=1,
                                    variant=ft.CardVariant.OUTLINED,
                                    content=ft.Column([pagination_controls],ft.MainAxisAlignment.CENTER)
                                ))
                            ),
                        ])
                    )
                )
            ],alignment=ft.MainAxisAlignment.START)

        )
        ]
    )
    update_page(page, 1)  # Mostrar la primera página inicialmente
    return ft.Row(
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        view_inventario
                    ]
                )
            )
        ]
    )

