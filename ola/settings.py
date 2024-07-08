import flet as ft
from components.rail import create_navigation_rail
import pymysql

# Configura la conexión a la base de datos
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
            ft.TextButton(text="Primero", on_click=lambda e: update_page(page, 1, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
        pagination_controls.controls.append(
            ft.TextButton(text="Anterior", on_click=lambda e: update_page(page, current_page - 1, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )

    for i in range(max(1, current_page - 2), min(total_pages + 1, current_page + 3)):
        pagination_controls.controls.append(
            ft.TextButton(text=str(i), on_click=lambda e, p=i: update_page(page, p, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
    
    if current_page < total_pages:
        pagination_controls.controls.append(
            ft.TextButton(text="Siguiente", on_click=lambda e: update_page(page, current_page + 1, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
        )
        pagination_controls.controls.append(
            ft.TextButton(text="Último", on_click=lambda e: update_page(page, total_pages, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value))
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

# Interfaz de usuario de Flet
def SettingsPage(page: ft.Page):
    global data_table, search_field, search_tip_prod_field, search_tip_esp_prod_field, pagination_controls
    page.title = "Paginación de Productos"

    data_table = ft.DataTable(
        width=1100,
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
        on_submit=lambda event: search_product(event, page)
    )
    
    search_tip_prod_field = ft.TextField(
        label="Buscar por Tipo de Producto",
        width=200,
        on_submit=lambda event: search_product(event, page)
    )
    
    search_tip_esp_prod_field = ft.TextField(
        label="Buscar por Tipo Específico de Producto",
        width=200,
        on_submit=lambda event: search_product(event, page)
    )

    # Botón para limpiar los campos de búsqueda
    clear_button = ft.TextButton(
        text="Limpiar",
        on_click=lambda event: clear_search_fields(event, page)
    )

    # Controles de paginación
    pagination_controls = ft.Row()
    update_pagination_controls(page)
    update_page(page, 1)  # Mostrar la primera página inicialmente

    return ft.Row(
        controls=[
            create_navigation_rail(page, selected_index=1),
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.Row([
                            search_field,
                            search_tip_prod_field,
                            search_tip_esp_prod_field,
                            clear_button,
                            current_page_label  # Indicador de la página actual
                        ]),
                        data_table,
                        pagination_controls
                    ]
                )
            )
        ]
    )
  