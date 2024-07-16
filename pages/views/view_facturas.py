import flet as ft
from components.rail import create_navigation_rail
import pymysql

def get_db_connection():
    return pymysql.connect(host="localhost", user="root", passwd="", db="billify")


# Consulta para obtener el número total de registros
def get_total_records_facturas():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM facturas")
    total_records = cursor.fetchone()[0]
    db.close()
    return total_records


# Parámetros de paginación
page_size = 10
total_records = get_total_records_facturas()
total_pages = (total_records + page_size - 1) // page_size  # Redondeo hacia arriba

# Variable para almacenar la página actual (se inicializará dentro de la función)
current_page_label = None


# Función para obtener datos de una página específica con filtros de búsqueda
def get_page_facturas(
    page, search_num_factura="", search_identificador="", search_fecha=""
):
    global total_pages  # Accede a la variable global total_pages
    offset = (page - 1) * page_size
    db = get_db_connection()
    cursor = db.cursor()

    query = """
    SELECT numero_factura, identificador, nombre, apellido, telefono, email, fecha 
    FROM facturas 
    WHERE 1
    """
    params = []

    if search_num_factura:
        query += " AND numero_factura LIKE %s"
        params.append("%" + search_num_factura + "%")
    if search_identificador:
        query += " AND identificador LIKE %s"
        params.append("%" + search_identificador + "%")
    if search_fecha:
        query += " AND fecha = %s"
        params.append(search_fecha)

    query += f" LIMIT {page_size} OFFSET {offset}"

    cursor.execute(query, params)
    data = cursor.fetchall()
    if len(data) == 0:
        print("Error: No se encontraron resultados para la búsqueda.")

    # Obtener el número total de registros después de aplicar los filtros
    cursor.execute(
        f"SELECT COUNT(*) FROM facturas WHERE 1 {'AND numero_factura LIKE %s' if search_num_factura else ''} {'AND identificador LIKE %s' if search_identificador else ''} {'AND fecha = %s' if search_fecha else ''}",
        params,
    )
    total_records_filtered = cursor.fetchone()[0]
    total_pages = (total_records_filtered + page_size - 1) // page_size  # Redondeo hacia arriba

    db.close()
    return data, total_records_filtered


# Función para actualizar los datos en la tabla
def update_page_facturas(
    page,
    page_number,
    search_num_factura="",
    search_identificador="",
    search_fecha="",
):
    global data_table, current_page_label  # Accede a las variables globales
    (
        data,
        total_records_filtered,
    ) = get_page_facturas(
        page_number, search_num_factura, search_identificador, search_fecha
    )
    data_table.rows.clear()
    for row in data:
        data_table.rows.append(
            ft.DataRow(
                cells=[
                    *[ft.DataCell(ft.Text(cell)) for cell in row],
                ]
            )
        ) # Eliminamos el boton de la tabla
    current_page_label.value = f"Página {page_number} de {total_pages}"
    page.update()
    update_pagination_controls(page, page_number, total_records_filtered)


def update_pagination_controls(
    page,
    current_page=1,
    total_records_filtered=None,
):
    global pagination_controls
    global search_num_factura_field
    global search_identificador_field
    global search_fecha_field 

    pagination_controls.controls.clear()

    if current_page > 1:
        pagination_controls.controls.append(
            ft.IconButton(
                icon=ft.icons.KEYBOARD_DOUBLE_ARROW_UP_OUTLINED,
                width=55,
                on_click=lambda e: update_page_facturas(
                    page,
                    1,
                    search_num_factura_field.value,
                    search_identificador_field.value,
                    search_fecha_field.value,
                ),
            )
        )
        pagination_controls.controls.append(
            ft.IconButton(
                icon=ft.icons.KEYBOARD_ARROW_UP_OUTLINED,
                width=55,
                on_click=lambda e: update_page_facturas(
                    page,
                    current_page - 1,
                    search_num_factura_field.value,
                    search_identificador_field.value,
                    search_fecha_field.value,
                ),
            )
        )

    for i in range(
        max(1, current_page - 2), min(total_pages + 1, current_page + 3)
    ):
        pagination_controls.controls.append(
            ft.TextButton(
                text=str(i),
                on_click=lambda e, p=i: update_page_facturas(
                    page,
                    p,
                    search_num_factura_field.value,
                    search_identificador_field.value,
                    search_fecha_field.value,
                ),
            )
        )

    if current_page < total_pages:
        pagination_controls.controls.append(
            ft.IconButton(
                icon=ft.icons.KEYBOARD_ARROW_DOWN_OUTLINED,
                width=55,
                on_click=lambda e: update_page_facturas(
                    page,
                    current_page + 1,
                    search_num_factura_field.value,
                    search_identificador_field.value,
                    search_fecha_field.value,
                ),
            )
        )
        pagination_controls.controls.append(
            ft.IconButton(
                icon=ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN_ROUNDED,
                width=55,
                on_click=lambda e: update_page_facturas(
                    page,
                    total_pages,
                    search_num_factura_field.value,
                    search_identificador_field.value,
                    search_fecha_field.value,
                ),
            )
        )

    page.update()

def search_factura(event, page):
    global search_num_factura_field
    global search_identificador_field
    global search_fecha_field
    
    search_num_factura = search_num_factura_field.value
    search_identificador = search_identificador_field.value
    search_fecha = search_fecha_field.value

    # Si todos los campos de búsqueda están vacíos, restablecer al estado original
    if not search_num_factura and not search_identificador and not search_fecha:
        update_page_facturas(page, 1)
    else:
        update_page_facturas(
            page, 1, search_num_factura, search_identificador, search_fecha
        )

def clear_search_fields(event, page):
    global search_num_factura_field
    global search_identificador_field
    global search_fecha_field 
    
    search_num_factura_field.value = ""
    search_identificador_field.value = ""
    search_fecha_field.value = ""
    search_factura(event, page) 

# Eliminamos open_factura_details


def view_facturas_all(page: ft.Page):

    global data_table,search_num_factura_field,search_identificador_field,search_fecha_field,pagination_controls,current_page_label

    page.padding = 0
    page.title = "Historias de Facturas"

    data_table = ft.DataTable( 
        width=1100,
        scale=0.99,
        columns=[
            ft.DataColumn(ft.Text("No. Factura")),
            ft.DataColumn(ft.Text("Identificador")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Fecha")),
            # ft.DataColumn(ft.Text("Detalles")), # Eliminamos la columna Detalles
        ],
        rows=[],
    )

    current_page_label = ft.Text(
        value="Página 1 de {}".format(total_pages)
    )  # Inicializa current_page_label aquí

    # Campos de búsqueda
    search_num_factura_field = ft.TextField(
        label="Buscar por No. Factura",
        width=200,
        height=40,
        content_padding=5,
        on_submit=lambda event: search_factura(event, page),
    )

    search_identificador_field = ft.TextField(
        label="Buscar por Identificador",
        width=200,
        height=40,
        content_padding=5,
        on_submit=lambda event: search_factura(event, page),
    )

    search_fecha_field = ft.TextField(
        label="Buscar por Fecha (YYYY-MM-DD)",
        width=200,
        height=40,
        content_padding=5,
        on_submit=lambda event: search_factura(event, page),
    )

    # Botón para limpiar los campos de búsqueda
    clear_button = ft.TextButton(
        text="Limpiar",
        on_click=lambda event: clear_search_fields(event, page),
    )

    # Controles de paginación
    pagination_controls = ft.Column(
        []
    )  # Inicializa pagination_controls aquí
    update_pagination_controls(page)

    Contenedor_rail = ft.Container(
        padding=0,
        width=140,
        height=650,
        content=ft.Card(
            variant=ft.CardVariant.OUTLINED,
            elevation=1,
            content=create_navigation_rail(page, selected_index=1),
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

    # Crear el botón de cambiar tema
    boton_dark_light_mode = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,  # Icono inicial del sol
        on_click=toggle_theme,
    )

    view_facturas = ft.Column(
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
                                                    ft.VerticalDivider(
                                                        color=ft.colors.TRANSPARENT
                                                    ),
                                                    ft.Icon(
                                                        name=ft.icons.RECEIPT_LONG_OUTLINED,
                                                        size=40,
                                                    ),
                                                    ft.VerticalDivider(),
                                                    ft.Text(
                                                        "Listado de Facturas",
                                                        weight=ft.FontWeight.W_900,
                                                        color="#3d5ff5",
                                                        size=18,
                                                    ),
                                                    ft.VerticalDivider(),
                                                ]
                                            ),
                                        ),
                                        ft.Container(
                                            height=60,
                                            width=900,
                                            alignment=ft.alignment.top_left,
                                            padding=0,
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(
                                                        color=ft.colors.TRANSPARENT
                                                    ),
                                                    boton_dark_light_mode,
                                                    search_num_factura_field,
                                                    search_identificador_field,
                                                    search_fecha_field,
                                                    clear_button,
                                                    current_page_label,  # Indicador de la página actual
                                                ]
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
            ),
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
                            alignment=ft.alignment.top_center,
                            content=ft.Container(
                                width=1221,
                                height=528,
                                alignment=ft.alignment.top_center,
                                content=ft.Row(
                                    [
                                        ft.Container(
                                            width=1100,
                                            padding=0,
                                            alignment=ft.alignment.top_center,
                                            content=(
                                                ft.Row(
                                                    spacing=0,
                                                    controls=[
                                                        data_table
                                                    ],
                                                )
                                            ),
                                        ),
                                        ft.Container(
                                            # Contenedor para los controles de paginación
                                            width=100,
                                            padding=0,
                                            height=528,
                                            alignment=ft.alignment.center,
                                            content=(
                                                ft.Card(
                                                    elevation=1,
                                                    variant=ft.CardVariant.OUTLINED,
                                                    content=ft.Column(
                                                        [
                                                            pagination_controls
                                                        ],
                                                        ft.MainAxisAlignment.CENTER,
                                                    ),
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
            ),
        ]
    )

    update_page_facturas(page, 1)  # Mostrar la primera página inicialmente

    return ft.Row(
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        view_facturas
                    ]
                )
            )
        ]
    )