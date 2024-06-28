import flet as ft
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
    
    # Obtener el número total de registros después de aplicar los filtros
    cursor.execute(f"SELECT COUNT(*) FROM productos WHERE 1 {'AND NOM_PROD LIKE %s' if search_query else ''} {'AND TIP_PROD = %s' if search_tip_prod else ''} {'AND TIP_ESP_PROD = %s' if search_tip_esp_prod else ''}", params)
    total_records_filtered = cursor.fetchone()[0]
    global total_pages
    total_pages = (total_records_filtered + page_size - 1) // page_size  # Redondeo hacia arriba
    
    db.close()
    return data

# Función de actualización de página
def update_page(page, page_num, search_query='', search_tip_prod='', search_tip_esp_prod=''):
    data_table.rows.clear()
    for row in get_page(page_num, search_query, search_tip_prod, search_tip_esp_prod):
        data_table.rows.append(
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row])
        )
    page.update()

    # Actualizar los controles de paginación según el número total de páginas
    update_pagination_controls(page)

def update_pagination_controls(page):
    pagination_controls.controls.clear()
    for i in range(1, total_pages + 1):
        pagination_controls.controls.append(ft.ElevatedButton(str(i), on_click=lambda e, p=i: update_page(page, p, search_field.value, search_tip_prod_field.value, search_tip_esp_prod_field.value)))

# Función para buscar productos por nombre, tipo de producto y tipo específico
def search_product(event, page):
    global total_pages
    
    search_query = search_field.value.strip()
    search_tip_prod = search_tip_prod_field.value.strip()
    search_tip_esp_prod = search_tip_esp_prod_field.value.strip()
    
    if not search_query and not search_tip_prod and not search_tip_esp_prod:
        # Si todos los campos están vacíos, mostrar todos los registros
        total_records = get_total_records()
        total_pages = (total_records + page_size - 1) // page_size  # Redondeo hacia arriba
        update_page(page, 1)
        
        return
    
    # Actualizar el total de registros basados en la búsqueda
    db = get_db_connection()
    cursor = db.cursor()
    
    query = "SELECT COUNT(*) FROM productos WHERE 1"
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
    
    cursor.execute(query, params)
    total_records = cursor.fetchone()[0]
    total_pages = (total_records + page_size - 1) // page_size  # Redondeo hacia arriba
    db.close()
    
    update_page(page, 1, search_query, search_tip_prod, search_tip_esp_prod)

# Interfaz de usuario de Flet
def main(page: ft.Page):
    global data_table, search_field, search_tip_prod_field, search_tip_esp_prod_field, pagination_controls
    page.title = "Paginación de Productos"

    data_table = ft.DataTable(
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

    # Controles de paginación
    pagination_controls = ft.Row()
    update_pagination_controls(page)

    page.add(
        ft.Row([
            search_field,
            search_tip_prod_field,
            search_tip_esp_prod_field,
        ]),
        data_table,
        pagination_controls
    )

    update_page(page, 1)  # Mostrar la primera página inicialmente

ft.app(target=main)
