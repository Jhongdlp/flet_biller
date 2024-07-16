import flet as ft
from components.rail import create_navigation_rail
from logic.validaciones import validar_cedula_ecuador,validar_pasaporte_ecuador,validar_ruc_ecuador
import pymysql
import re

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'billify'
}


def validar_email(email):
    """Verifica si un email tiene formato válido usando expresiones regulares."""
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(regex, email))

def validar_telefono(telefono):
    """Verifica si un teléfono tiene 10 dígitos numéricos."""
    return len(telefono) == 10 and telefono.isdigit()

def obtener_datos_cliente(escoger_identificador, cedula_campo_textfield, nombre_cliente_textfield,
                      apellido_cliente_textfield, direccion_cliente_textfield,
                      telefono_cliente_textfield, mail_cliente_textfield):
    """Valida los datos del cliente y devuelve un diccionario con la información."""
    datos_cliente = {}
    error_mensaje = None
    
    if not all([cedula_campo_textfield.value, nombre_cliente_textfield.value,
               apellido_cliente_textfield.value, direccion_cliente_textfield.value,
               telefono_cliente_textfield.value, mail_cliente_textfield.value]):
        error_mensaje = "Por favor, complete todos los campos."
        return None, error_mensaje

    identificador = cedula_campo_textfield.value
    tipo_id = escoger_identificador.value

    if tipo_id == "Cedula":
        if not validar_cedula_ecuador(identificador):
            error_mensaje = "La cédula ingresada no es válida."
        identificador = f"C.{identificador}"
    elif tipo_id == "RUC":
        if not validar_ruc_ecuador(identificador):
            error_mensaje = "El RUC ingresado no es válido."
        identificador = f"R.{identificador}"
    elif tipo_id == "Pasaporte":
        if not validar_pasaporte_ecuador(identificador):
            error_mensaje = "El pasaporte ingresado no es válido."
        identificador = f"P.{identificador}"
    else:
        error_mensaje = "Seleccione un tipo de identificación válido."

    if not validar_email(mail_cliente_textfield.value):
        error_mensaje = "El email ingresado no es válido."
    if not validar_telefono(telefono_cliente_textfield.value):
        error_mensaje = "El teléfono debe tener 10 dígitos numéricos."

    if error_mensaje:
        return None, error_mensaje

    datos_cliente["identificador"] = identificador
    datos_cliente["nombre_apellido"] = f"{nombre_cliente_textfield.value} {apellido_cliente_textfield.value}"
    datos_cliente["direccion"] = direccion_cliente_textfield.value
    datos_cliente["telefono"] = telefono_cliente_textfield.value
    datos_cliente["email"] = mail_cliente_textfield.value

    return datos_cliente, None
#------------------------FUNCION BUSCAR EN LA BASE DE DATOS-------------------------
def buscar_clientes_por_cedula(page, cedula):
    page.title="Clientes"
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        consulta = "SELECT * FROM clientes WHERE identificador = %s"
        cursor.execute(consulta, (f"C.{cedula}",))
        resultados = cursor.fetchall()
        return resultados
    except pymysql.Error as e:
        print(f"Error al buscar clientes: {e}")
        page.snack_bar = ft.SnackBar(ft.Text("Error al buscar clientes."))
        page.snack_bar.open = True
        page.update()
        return []
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()
#------------------------FUNCION BUSCAR EN LA BASE DE DATOS-------------------------
def buscar_clientes_por_ruc(page, ruc):
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        consulta = "SELECT * FROM clientes WHERE identificador = %s"
        cursor.execute(consulta, (f"R.{ruc}",))
        resultados = cursor.fetchall()
        return resultados
    except pymysql.Error as e:
        print(f"Error al buscar clientes: {e}")
        page.snack_bar = ft.SnackBar(ft.Text("Error al buscar clientes."))
        page.snack_bar.open = True
        page.update()
        return []
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

#------------------------FUNCION BUSCAR EN LA BASE DE DATOS-------------------------
def buscar_clientes_por_pasaporte(page, pasaporte):
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        consulta = "SELECT * FROM clientes WHERE identificador = %s"
        cursor.execute(consulta, (f"P.{pasaporte}",))
        resultados = cursor.fetchall()
        return resultados
    except pymysql.Error as e:
        print(f"Error al buscar clientes: {e}")
        page.snack_bar = ft.SnackBar(ft.Text("Error al buscar clientes."))
        page.snack_bar.open = True
        page.update()
        return []
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()  

def view_clientes_all(page: ft.page):
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

    def limpiar_error_telefono(e):
        if telefono_cliente_texfield.error_text: # Si hay un error...
            telefono_cliente_texfield.error_text = None # ... se elimina
            page.update() 
    def limpiar_error_mail(e):
        if mail_cliente_texfield.error_text: # Si hay un error...
            mail_cliente_texfield.error_text = None # ... se elimina
            page.update() 
    def limpiar_error_identificador(e):
        if cedula_campo_texfild.error_text: # Si hay un error...
            cedula_campo_texfild.error_text = None # ... se elimina
            page.update() 

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
    cedula_campo_texfild = ft.TextField(
        hint_text="identificador", 
        content_padding=5, 
        width=250,
        height=35, 
        on_change=lambda e: limpiar_error_identificador(e)

    ) 
    nombre_cliente_texfield=ft.TextField(hint_text="Nombre del cliente",
        content_padding=5,
        width=175,  
        height=35,  
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[a-zA-Z\s]",  # Letras minúsculas, mayúsculas y espacios
            replacement_string="",
        ),         
    )   
    apellido_cliente_texfield=ft.TextField(hint_text="Apellido del cliente",
        content_padding=5,
        width=175,
        height=35,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[a-zA-Z\s]",  # Letras minúsculas, mayúsculas y espacios
            replacement_string="",
        ),
    )
    direccion_cliente_texfield=ft.TextField(hint_text="Direccion",
        content_padding=5,
        min_lines=3, # Controla la altura visible
        max_lines=3,
        #height=100, # Define la altura fija
        width=360,
        max_length=150,  
        #height=35,           
    )
    telefono_cliente_texfield=ft.TextField(
        hint_text="Telefono del cliente",
        content_padding=5,
        width=115,  
        height=35,     
        on_change=lambda e: limpiar_error_telefono(e)
    )
    mail_cliente_texfield=ft.TextField(hint_text="Mail del cliente",
        content_padding=5,
        width=240,
        height=35,
        on_change=lambda e: limpiar_error_mail(e)
    )
    Escoger_identificador=ft.Dropdown(
        width=100,
        height=35,
        content_padding=1,
        options=[
            ft.dropdown.Option("Cedula"),
            ft.dropdown.Option("RUC"),
            ft.dropdown.Option("Pasaporte"),
        ],     
    )

    def guardar_cliente(e):
        datos_cliente, error_mensaje = obtener_datos_cliente(
            Escoger_identificador,
            cedula_campo_texfild,
            nombre_cliente_texfield,
            apellido_cliente_texfield,
            direccion_cliente_texfield,
            telefono_cliente_texfield,
            mail_cliente_texfield
        )
        # --- Validación adicional para errores de los textfield ---
        if error_mensaje:
            if "cédula" in error_mensaje.lower():
                cedula_campo_texfild.error_text = error_mensaje
            if "ruc" in error_mensaje.lower():
                cedula_campo_texfild.error_text = error_mensaje
            if "pasaporte" in error_mensaje.lower():
                cedula_campo_texfild.error_text = error_mensaje
            if "nombre" in error_mensaje.lower():
                nombre_cliente_texfield.error_text = error_mensaje
            if "apellido" in error_mensaje.lower():
                apellido_cliente_texfield.error_text = error_mensaje
            if "dirección" in error_mensaje.lower() or "direccion" in error_mensaje.lower():
                direccion_cliente_texfield.error_text = error_mensaje
            if "teléfono" in error_mensaje.lower() or "telefono" in error_mensaje.lower():
                telefono_cliente_texfield.error_text = error_mensaje
            if "email" in error_mensaje.lower():
                mail_cliente_texfield.error_text = error_mensaje

            page.snack_bar = ft.SnackBar(ft.Text(error_mensaje))
            page.snack_bar.open = True
            page.update()
            return

        # -- CONEXIÓN A LA BASE DE DATOS --
        try:
            connection = pymysql.connect(**db_config)
            cursor = connection.cursor()

            # Consulta SQL para insertar el cliente
            sql = "INSERT INTO clientes (identificador, nombre_apellido, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)"
            valores = (datos_cliente["identificador"], datos_cliente["nombre_apellido"],
                      datos_cliente["direccion"], datos_cliente["telefono"], datos_cliente["email"])

            cursor.execute(sql, valores)
            connection.commit()

            # Éxito al guardar:
            page.snack_bar = ft.SnackBar(ft.Text("Cliente guardado correctamente."))
            page.snack_bar.open = True

            # Limpiar campos después de guardar
            cedula_campo_texfild.value = ""
            nombre_cliente_texfield.value = ""
            apellido_cliente_texfield.value = ""
            direccion_cliente_texfield.value = ""
            telefono_cliente_texfield.value = ""
            mail_cliente_texfield.value = ""

            page.update()

        except pymysql.Error as e:
            # Error al guardar
            print(f"Error al conectar a la base de datos: {e}")
            page.snack_bar = ft.SnackBar(ft.Text("Error al guardar el cliente."))
            page.snack_bar.open = True
            page.update()
        finally:
            if connection and connection.open:
                cursor.close()
                connection.close()
    # --- TextFields para la búsqueda ---
    buscar_cedula_textfield = ft.TextField(label="Buscar por cédula", width=250, on_submit=lambda e: buscar_cliente(e)
        ,max_length=10
    )
    buscar_ruc_textfield = ft.TextField(label="Buscar por RUC", width=250,on_submit=lambda e: buscar_cliente(e),max_length=13)
    buscar_pasaporte_textfield = ft.TextField(label="Buscar por pasaporte", width=250,on_submit=lambda e: buscar_cliente(e),max_length=30)
    
    def Limpiar_agregar_clientes(e):
        cedula_campo_texfild.value = ""
        nombre_cliente_texfield.value = ""
        apellido_cliente_texfield.value = ""
        direccion_cliente_texfield.value = ""
        telefono_cliente_texfield.value = ""
        mail_cliente_texfield.value = ""

        page.update()
    # --- DataTable para mostrar los resultados ---
    tabla_clientes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Identificador")),
            ft.DataColumn(ft.Text("Nombre y Apellido")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Email"))
        ],
        rows=[]  # Inicialmente vacío
    )

    def buscar_cliente(e):
        # --- Obtener el término de búsqueda ---
        if e.control == buscar_cedula_textfield:
            termino_busqueda = buscar_cedula_textfield.value
            resultados = buscar_clientes_por_cedula(page, termino_busqueda)
        elif e.control == buscar_ruc_textfield:
            termino_busqueda = buscar_ruc_textfield.value
            resultados = buscar_clientes_por_ruc(page, termino_busqueda)
        elif e.control == buscar_pasaporte_textfield:
            termino_busqueda = buscar_pasaporte_textfield.value
            resultados = buscar_clientes_por_pasaporte(page, termino_busqueda)
        else:
            print("Control de evento desconocido")  
            return
        
        # --- Actualizar la tabla con los resultados ---
        tabla_clientes.rows.clear()  # Limpiar resultados anteriores

        if resultados:
            for resultado in resultados:
                tabla_clientes.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(resultado[0])),  # ID
                            ft.DataCell(ft.Text(resultado[1])),  # Identificador
                            ft.DataCell(ft.Text(resultado[2])),  # Nombre y Apellido
                            ft.DataCell(ft.Text(resultado[4])),  # Teléfono
                            ft.DataCell(ft.Text(resultado[5]))   # Email
                        ]
                    )
                )
        else:
            # Mostrar SnackBar si no hay resultados
            page.snack_bar = ft.SnackBar(ft.Text("No se encontraron clientes con ese término de búsqueda."))
            page.snack_bar.open = True
            page.update()

        page.update()
    page.update()

    def limpiar_busqueda(e):
        buscar_cedula_textfield.value = ""
        buscar_ruc_textfield.value = ""
        buscar_pasaporte_textfield.value = ""
        tabla_clientes.rows.clear()
        page.update()

    view_clientes = ft.Column(
        [
            ft.Container(
                padding=0,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            height=60,
                            width=1365,
                            # border=ft.border.all(color='#737780'),
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
                                            # border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                    ft.Icon(name=ft.icons.GROUP_OUTLINED, size=40),
                                                    ft.VerticalDivider(),
                                                    ft.Text(
                                                        "Clientes",
                                                        weight=ft.FontWeight.W_900,
                                                        color="#3d5ff5",
                                                        size=18,
                                                    ),
                                                    # ft.Text("    "),
                                                    ft.VerticalDivider(),
                                                ]
                                            ),
                                        ),
                                        ft.Container(
                                            height=60,
                                            width=320,
                                            # border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                            content=ft.Row(
                                                [
                                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                                    boton_dark_light_mode,
                                                    ft.ElevatedButton("limpiar",on_click=lambda e: limpiar_busqueda(e)),
                                                ]
                                            ),
                                        ),
                                    ]
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
                            width=1200,
                            height=650,
                            # border=ft.border.all(),
                            alignment=ft.alignment.top_left,
                            content=ft.Row(
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        width=400,
                                        height=600,
                                        # border=ft.border.all(),
                                        # padding=5,
                                        alignment=ft.alignment.top_center,
                                        content=ft.Container(
                                            width=395,
                                            height=525,
                                            # border=ft.border.all(),
                                            content=ft.Card(
                                                variant=ft.CardVariant.OUTLINED,
                                                elevation=10,
                                                content=ft.Column(
                                                    [
                                                        ft.Container(
                                                            width=395,
                                                            alignment=ft.alignment.center,
                                                            padding=10,
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(
                                                                        "  Agregar Cliente",
                                                                        weight=ft.FontWeight.W_900,
                                                                        size=25,
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                        ft.Divider(),
                                                        ft.Container(
                                                            width=395,
                                                            alignment=ft.alignment.center,
                                                            padding=10,
                                                            content=ft.Column(
                                                                [
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center_left,
                                                                        content=ft.Row(
                                                                            [
                                                                                ft.Column(
                                                                                    [
                                                                                        ft.Text(
                                                                                            "Identificador:",
                                                                                            weight=ft.FontWeight.W_900,
                                                                                            size=14,
                                                                                        ),
                                                                                        ft.Row(
                                                                                            [
                                                                                                Escoger_identificador,
                                                                                                cedula_campo_texfild,
                                                                                            ]
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    ft.Row(
                                                                        [
                                                                            ft.Column(
                                                                                [
                                                                                    ft.Text(
                                                                                        "Nombre:",
                                                                                        weight=ft.FontWeight.W_900,
                                                                                        size=14,
                                                                                    ),
                                                                                    nombre_cliente_texfield,
                                                                                ]
                                                                            ),
                                                                            ft.Column(
                                                                                [
                                                                                    ft.Text(
                                                                                        "Apellido:",
                                                                                        weight=ft.FontWeight.W_900,
                                                                                        size=14,
                                                                                    ),
                                                                                    apellido_cliente_texfield,
                                                                                ]
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    ft.Column(
                                                                        [
                                                                            ft.Text(
                                                                                "Direccion:",
                                                                                weight=ft.FontWeight.W_900,
                                                                                size=14,
                                                                            ),
                                                                            direccion_cliente_texfield,
                                                                        ]
                                                                    ),
                                                                    ft.Row(
                                                                        [
                                                                            ft.Column(
                                                                                [
                                                                                    ft.Text(
                                                                                        "Telefono:",
                                                                                        weight=ft.FontWeight.W_900,
                                                                                        size=14,
                                                                                    ),
                                                                                    telefono_cliente_texfield,
                                                                                ]
                                                                            ),
                                                                            ft.Column(
                                                                                [
                                                                                    ft.Text(
                                                                                        "mail:",
                                                                                        weight=ft.FontWeight.W_900,
                                                                                        size=14,
                                                                                    ),
                                                                                    mail_cliente_texfield,
                                                                                ]
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    ft.Divider(height=3),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.top_right,
                                                                        content=ft.Row(
                                                                            [
                                                                                ft.ElevatedButton(
                                                                                    "Limpiar",
                                                                                    bgcolor=ft.colors.RED_600,
                                                                                    color=ft.colors.WHITE,
                                                                                    on_click=Limpiar_agregar_clientes
                                                                                ),
                                                                                ft.ElevatedButton(
                                                                                    "Guardar cliente",
                                                                                    bgcolor=ft.colors.GREEN_600,
                                                                                    color=ft.colors.WHITE,
                                                                                    on_click=guardar_cliente,
                                                                                ),
                                                                            ],
                                                                            ft.MainAxisAlignment.END,
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ],
                                                )
                                            ),
                                        ),
                                    ),
                                    ft.Container(
                                        width=800,
                                        height=600,
                                        # border=ft.border.all(),
                                        alignment=ft.alignment.center,
                                        content=ft.Column(
                                            [
                                                ft.Container(
                                                    width=795,
                                                    # height=50,
                                                    #border=ft.border.all(),
                                                    padding=10,
                                                    content=ft.Container(
                                                        ft.Column(
                                                            [
                                                                ft.Text(
                                                                    "Busca a un cliente:",
                                                                    weight=ft.FontWeight.W_900,
                                                                    size=25,
                                                                ),
                                                                ft.Row(
                                                                    [
                                                                        buscar_cedula_textfield,
                                                                        buscar_ruc_textfield,
                                                                        buscar_pasaporte_textfield,
                                                                    ]
                                                                ),
                                                                ft.Divider(),
                                                            ]
                                                        ),
                                                    ),
                                                ),
                                                ft.Container(width=795, content=tabla_clientes),
                                            ]
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
            ),
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
                        view_clientes
                    ]
                )
            )
        ]
    )

