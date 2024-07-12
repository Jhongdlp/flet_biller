import flet as ft
from components.rail import create_navigation_rail
import pymysql
import re

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'billify'
}

def validar_cedula_ecuador(cedula):
    """Verifica si una cédula ecuatoriana es válida."""
    if len(cedula) != 10 or not cedula.isdigit():
        return False
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    digito_verificador = int(cedula[9])
    suma = sum([int(cedula[i]) * coeficientes[i] if int(cedula[i]) * coeficientes[i] < 10 else int(cedula[i]) * coeficientes[i] - 9 for i in range(9)])
    resultado = 10 - (suma % 10)
    return resultado == digito_verificador

def validar_ruc_ecuador(ruc):
    """Verifica si un RUC ecuatoriano es válido."""
    print(f"RUC recibido: {ruc}")
    if len(ruc) != 13 or not ruc.isdigit():
        print("Error: Longitud o formato incorrecto")
        return False

    # Verificar el tercer dígito (tipo de persona)
    tipo_persona = int(ruc[2])
    print(f"Tipo de persona: {tipo_persona}")
    if tipo_persona not in [0, 1, 2, 3, 4, 5, 6, 9]:
        print("Error: Tipo de persona inválido")
        return False

    # Coeficientes de acuerdo al tipo de persona
    if tipo_persona in [0, 1, 2, 3, 4, 5]:  # Persona natural
        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        modulo = 10
        digito_verificador = int(ruc[9])  # Obtener el décimo dígito
    elif tipo_persona == 6:  # Entidad pública
        coeficientes = [3, 2, 7, 6, 5, 4, 3, 2]
        modulo = 11
        digito_verificador = int(ruc[8])  # Obtener el noveno dígito
    elif tipo_persona == 9:  # Sociedad privada o extranjera
        coeficientes = [4, 3, 2, 7, 6, 5, 4, 3, 2]
        modulo = 11
        digito_verificador = int(ruc[9])  # Obtener el décimo dígito
    else:
        print("Error: Tipo de persona inválido")
        return False

    print(f"Coeficientes usados: {coeficientes}")

    # Validación
    suma = 0
    for i in range(len(coeficientes)):
        producto = int(ruc[i]) * coeficientes[i]
        if tipo_persona in [0, 1, 2, 3, 4, 5] and producto >= 10:
            producto -= 9
        suma += producto
    print(f"Suma ponderada: {suma}")

    residuo = suma % modulo
    print(f"Residuo: {residuo}")

    resultado = 0 if residuo == 0 else modulo - residuo
    print(f"Resultado (antes de validar el último dígito): {resultado}")

    # Validación del último dígito
    if resultado != digito_verificador:
        print(f"Error: El dígito verificador no coincide: {resultado} != {digito_verificador}")
        return False

    print("RUC válido")
    return True



def validar_pasaporte_ecuador(pasaporte):
    """Placeholder para validación de pasaporte (flexible para extranjeros)."""
    # Agrega tu lógica aquí si necesitas un formato específico
    return True

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
    cedula_campo_texfild = ft.TextField(
        hint_text="Cedula", 
        content_padding=5, 
        width=250,
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
    )
    mail_cliente_texfield=ft.TextField(hint_text="Mail del cliente",
        content_padding=5,
        width=240,
        height=35
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
                                                                Escoger_identificador,cedula_campo_texfild,
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
                                                        ft.ElevatedButton("Guardar cliente",bgcolor=ft.colors.GREEN_600,color=ft.colors.WHITE
                                                            ,on_click=guardar_cliente
                                                        ), 
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