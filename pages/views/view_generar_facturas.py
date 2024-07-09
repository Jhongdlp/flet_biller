import flet as ft
import re
from components.rail import create_navigation_rail
from sql.base_implemtnacion import get_product_data

def generar_factura_pro(page: ft.Page):
    #!==================================================================================
    #!=                                                                                =
    #!=                                 PAGINA TRES                                     =
    #!=                                                                                =
    #!==================================================================================    
    # Inicializar el color de fondo del contenedor y el modo de la página
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=0
    Contenedor_rail =ft.Container(padding=0,
        width=140,
        height=650,
        content=ft.Card(
                #margin=5,
                variant=ft.CardVariant.OUTLINED,
                elevation=1,
                content=create_navigation_rail(page, selected_index=2)
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



    
    #!=================TEXFIELDS==================
    # Definir la función que se ejecutará al cambiar el texto

    cedula_cliente_texfield=ft.TextField(label=("Cedula"),width=230,height=45,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        error_text=None,  # No mostrar error inicialmente
    )
    nombre_cliente_texfield=ft.TextField(label=("Nombre"),width=230,height=45,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[a-zA-Z\s]",  # Letras minúsculas, mayúsculas y espacios
            replacement_string="",
        ),
        error_text=None,  # No mostrar error inicialmente                                     
    )
    apellido_cliente_texfield=ft.TextField(label=("Apellido"),width=230,height=45,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[a-zA-Z\s]",  # Letras minúsculas, mayúsculas y espacios
            replacement_string="",
        ),
        error_text=None,  # No mostrar error inicialmente
    )
    direccion_cliente_texfield=ft.TextField(label=("Direccion"),width=230,height=45,

    )
    telefono_cliente_texfield=ft.TextField(label=("Telefono"),width=230,height=45,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")                                       
    )

    mail_cliente_texfield=ft.TextField(label=("E-Mail"),width=475,height=45)

    id_producto = ft.TextField(width=150,height=30,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        content_padding=5                          
    )
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def on_generar_factura_click(e):
        """
        Valida los campos y genera la factura XML y PDF si todo es correcto.
        """

        # Validar campos de cliente
        error = False
        if not cedula_cliente_texfield.value:
            cedula_cliente_texfield.error_text = "Este campo es obligatorio"
            cedula_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            cedula_cliente_texfield.error_text = None  # Limpiar error si se corrige

        if not nombre_cliente_texfield.value:
            nombre_cliente_texfield.error_text = "Este campo es obligatorio"
            nombre_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            nombre_cliente_texfield.error_text = None

        if not apellido_cliente_texfield.value:
            apellido_cliente_texfield.error_text = "Este campo es obligatorio"
            apellido_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            apellido_cliente_texfield.error_text = None

        if not direccion_cliente_texfield.value:
            direccion_cliente_texfield.error_text = "Este campo es obligatorio"
            direccion_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            direccion_cliente_texfield.error_text = None

        if not telefono_cliente_texfield.value:
            telefono_cliente_texfield.error_text = "Este campo es obligatorio"
            telefono_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            telefono_cliente_texfield.error_text = None

        if not mail_cliente_texfield.value:
            mail_cliente_texfield.error_text = "Este campo es obligatorio"
            mail_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        elif not is_valid_email(mail_cliente_texfield.value):
            mail_cliente_texfield.error_text = "Ingrese un correo electrónico válido"
            mail_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            mail_cliente_texfield.error_text = None

        # Validar si hay productos en la tabla
        if not data_table.rows:
            page.snack_bar = ft.SnackBar(
                ft.Text("No hay productos en la factura.", size=15),
                bgcolor=ft.colors.RED_400,
                duration=3000
            )
            page.snack_bar.open = True
            error = True

        # Actualizar la interfaz para mostrar los errores (si los hay)
        page.update()

        # Si no hay errores, continuar con la generación de la factura
        if not error:
            # ... (Lógica para generar factura XML y PDF usando los datos de los campos y la tabla)
            print("¡Factura generada con éxito!") 

    def on_change(e):
        if cedula_cliente_texfield.error_text:
            cedula_cliente_texfield.error_text = None
            cedula_cliente_texfield.update()

        if nombre_cliente_texfield.error_text:
            nombre_cliente_texfield.error_text = None
            nombre_cliente_texfield.update()

        if apellido_cliente_texfield.error_text:
            apellido_cliente_texfield.error_text = None
            apellido_cliente_texfield.update()

        if direccion_cliente_texfield.error_text:
            direccion_cliente_texfield.error_text = None
            direccion_cliente_texfield.update()

        if telefono_cliente_texfield.error_text:
            telefono_cliente_texfield.error_text = None
            telefono_cliente_texfield.update()

        if mail_cliente_texfield.error_text:
            mail_cliente_texfield.error_text = None
            mail_cliente_texfield.update()

    # Asociar la función on_change al evento on_change de los TextField
    cedula_cliente_texfield.on_change = on_change
    nombre_cliente_texfield.on_change = on_change
    apellido_cliente_texfield.on_change = on_change
    direccion_cliente_texfield.on_change = on_change
    telefono_cliente_texfield.on_change = on_change
    mail_cliente_texfield.on_change = on_change

    subtotal_value = ft.Text(value="0.00")
    iva_value = ft.Text(value="0.00")
    total_value = ft.Text(value="0.00")

    data_table = ft.DataTable(
        width=800,
        column_spacing=15,
        columns=[
            ft.DataColumn(ft.Text("No."), tooltip="Número de fila"),
            ft.DataColumn(ft.Text("ID"), tooltip="ID del Producto"),
            ft.DataColumn(ft.Text("Nombre"), tooltip="Nombre del Producto"),
            ft.DataColumn(ft.Text("Tipo"), tooltip="Tipo del Producto"),
            ft.DataColumn(ft.Text("Iva"), tooltip="IVA del Producto"),
            ft.DataColumn(ft.Text("Precio"), tooltip="Precio del Producto"),
            ft.DataColumn(ft.Text("Cantidad"), tooltip="Cantidad"),
            ft.DataColumn(ft.Text("Acción"), tooltip="Acciones disponibles")
        ],
        rows=[],
    )

    scrollable_container = ft.Container(
        height=450,
        content=ft.Column([data_table], scroll=ft.ScrollMode.AUTO)
    )

    def update_row_numbers():
        for i, row in enumerate(data_table.rows):
            row.cells[0] = ft.DataCell(ft.Text(str(i + 1)))

    def calculate_subtotal():
        subtotal = 0.0
        for row in data_table.rows:
            cantidad_str = row.cells[6].content.value
            cantidad = int(cantidad_str) if cantidad_str.isdigit() else 0
            precio = float(row.cells[5].content.value)
            subtotal += cantidad * precio
        subtotal_value.value = f"{subtotal:.2f}"
        iva = subtotal * 0.12
        iva_value.value = f"{iva:.2f}"
        total_value.value = f"{subtotal + iva:.2f}"
        page.update()

    def add_product(e):
        product_id = id_producto.value
        if not product_id.isdigit():
            print("Error: El ID del producto debe ser mayor a 0.")
            id_producto.focus()
            return

        product_data = get_product_data(product_id)

        if not product_data:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: El producto con ID {product_id} no se encontró en la base de datos.",
                size=20),
                bgcolor=ft.colors.RED_400,
                duration=2000,
            )
            page.snack_bar.open = True
            id_producto.focus()
            page.update()
            return

        for row in data_table.rows:
            if row.cells[1].content.value == product_data[0]:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"El producto con ID {product_data[0]} ya ha sido  agregado.",size=20,color=ft.colors.WHITE),
                    bgcolor=ft.colors.BLUE_800,
                    duration=2000,
                    show_close_icon=True,
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

        cantidad_producto = ft.TextField(value="1", width=50,height=40,
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
            max_length=4,
            content_padding=2,
            text_align=ft.TextAlign.CENTER,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.colors.TRANSPARENT,
            filled=True,                                  
        )

        def validate_cantidad(e):
            if not cantidad_producto.value.isdigit():
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser un número."),duration=2000,
                )
                page.snack_bar.open = True
                page.update()
                return

            cantidad = int(cantidad_producto.value)
            existencias = product_data[5]

            if cantidad <= 0:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser mayor que cero."),duration=2000,                       
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

            if cantidad > existencias:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad ingresada {cantidad} excede las existencias disponibles {existencias} para el producto {product_data[1]} (ID: {product_data[0]})."),
                    duration=2000,
                )
                page.snack_bar.open = True
                page.update()
                return

            calculate_subtotal()

        cantidad_producto.on_change = validate_cantidad

        new_row = ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(len(data_table.rows) + 1))),
            ft.DataCell(ft.Text(product_data[0])),
            ft.DataCell(ft.Text(product_data[1])),
            ft.DataCell(ft.Text(product_data[2])),
            ft.DataCell(ft.Text(product_data[3])),
            ft.DataCell(ft.Text(product_data[4])),
            ft.DataCell(cantidad_producto),
            ft.DataCell(ft.IconButton(
                icon=ft.icons.DELETE_FOREVER,
                tooltip="Eliminar producto",
                on_click=lambda e: delete_product(e, new_row)
            ))
        ])
        data_table.rows.append(new_row)
        id_producto.value = ""
        id_producto.focus()  # Establece el foco en el TextField después de agregar el producto
        page.update()
        calculate_subtotal()

    def delete_product(e, row):
        data_table.rows.remove(row)
        update_row_numbers()
        page.update()
        calculate_subtotal()

    def delete_all_rows(e):
        data_table.rows.clear()
        update_row_numbers()
        page.update()
        calculate_subtotal()

    id_producto.on_submit = add_product

    def abrir_dialogo_pago(e):
        """Abre el AlertDialog para gestionar el pago."""

        def calcular_cambio(e):
            """Calcula el cambio cuando cambia el valor de 'dinero_input'."""
            try:
                dinero_ingresado = float(dinero_input.value)
                cambio = dinero_ingresado - float(total_value.value)
                cambio_text.value = f"Cambio: {cambio:.2f}"
            except ValueError:
                cambio_text.value = "Ingresa un número válido"
            page.update()

        # Crear los controles del AlertDialog
        dinero_input = ft.TextField(label="Dinero Ingresado", on_change=calcular_cambio)
        cambio_text = ft.Text("Cambio: 0.00")
        total_productos_text = ft.Text(f"Total de productos: {len(data_table.rows)}")

        # Crear el AlertDialog
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Pago"),
            content=ft.Column(
                [
                    dinero_input,
                    cambio_text,
                    total_productos_text,
                ]
            ),
            actions=[
                ft.ElevatedButton(
                    text="Cerrar", 
                    on_click=lambda e: (
                        setattr(dlg, "open", False),  # Asignar False a dlg.open
                        page.update()
                    )
                ),
            ],
        )

        # Abrir el AlertDialog
        page.dialog = dlg
        dlg.open = True
        page.update()

    
    def cerrar_alert_metodo_de_pago(e):
        alert_metodo_pago.open = False
        page.update()

    alert_metodo_pago = ft.AlertDialog(
        modal=False,
        title=ft.Text("Elige el metodo de pago"),
        content=ft.Container(
            height=240,
            content=ft.Column(spacing=0,controls=[
                ft.Container(
                    content=ft.Text("Targeta de credito",size=20,color=ft.colors.WHITE),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_600,
                    width=350,
                    height=60,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Targeta de debito",size=20,color=ft.colors.WHITE),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.PURPLE_600,
                    width=350,
                    height=60,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Pago en efectivo",size=20,color=ft.colors.WHITE),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_600,
                    width=350,
                    height=60,
                    border_radius=10,
                    on_click=abrir_dialogo_pago,
                ),
            ])
        ),
        actions_alignment=ft.MainAxisAlignment.END,
    )
    def abrir_alert_metodo_pago(e):
        page.dialog = alert_metodo_pago
        alert_metodo_pago.open = True
        page.update()
    
   
    delete_all_button = ft.ElevatedButton(text="Eliminar todas las filas", on_click=delete_all_rows)

    Boton_consumirdor_final=ft.ElevatedButton("Consumidor final",width=158,height=35,bgcolor=ft.colors.GREEN_500,color="WHITE",
        #on_click=Boton_Consumidor_final_logica
        )
    Boton_Eliminar_Datos=ft.ElevatedButton("Eliminar Datos",width=147,height=35,bgcolor=ft.colors.RED,color=ft.colors.WHITE,
        #on_click=Boton_Eliminar_Datos_logica
        )
    card_totales_generar=ft.Card(elevation=5,content=ft.Container(
        width=170,
        height=135,
        padding=10,
        content=ft.Column(spacing=0,controls=[
            ft.Row([ft.Text("Subtotal: "), subtotal_value]),
            ft.Row([ft.Text("Iva: "), iva_value]),
            ft.Row([ft.Text("Total: "), total_value]),
            ft.Divider(color=ft.colors.TRANSPARENT),
            ft.ElevatedButton("Generar Factura",
            width=160,
            height=35,
            bgcolor=ft.colors.INDIGO_600,
            color=ft.colors.WHITE,
            on_click=abrir_alert_metodo_pago
            ),
            ft.Divider(color=ft.colors.TRANSPARENT),
        ])
    ))
    page_three_ui=ft.Column([
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
                                    ft.Icon(name=ft.icons.LIBRARY_ADD_OUTLINED,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Nueva factura",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    #ft.Text("    "),
                                    ft.VerticalDivider(),
                                    
                                ])
                            ),
                            ft.Container(height=60,width=320,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    boton_dark_light_mode
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
                    content=ft.Column(spacing=0,controls=[
                        ft.Row(spacing=0,controls=[
                            ft.Container(width=500,height=600,
                                #border=ft.border.all(),
                                content=ft.Column(spacing=0,controls=[
                                    ft.Text("Datos de cliente",size=25),
                                    ft.Divider(),
                                        ft.Row(spacing=0,controls=[
                                            cedula_cliente_texfield,
                                            ft.IconButton(icon=ft.icons.DOCUMENT_SCANNER),
                                            ft.IconButton(icon=ft.icons.DOCK)
                                        ]),
                                        ft.Divider(),
                                        ft.Row(spacing=0,controls=[
                                            nombre_cliente_texfield,
                                            ft.VerticalDivider(),
                                            apellido_cliente_texfield
                                        ]),
                                        ft.Divider(),
                                        ft.Row(spacing=0,controls=[
                                            direccion_cliente_texfield,
                                            ft.VerticalDivider(),
                                            telefono_cliente_texfield
                                        ]),
                                        ft.Divider(),
                                        ft.Row(spacing=0,controls=[
                                            mail_cliente_texfield
                                        ]),
                                    ft.Divider(),
                                    ft.Container(
                                        width=500,
                                        height=200,  # Puedes ajustar la altura según tus necesidades
                                        alignment=ft.alignment.bottom_center,
                                        #border=ft.border.all(),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            width=320,
                                                            height=215,
                                                            padding=0,
                                                            alignment=ft.alignment.bottom_center,
                                                            #border=ft.border.all(),
                                                            content=ft.Row(spacing=6,controls=[
                                                                Boton_Eliminar_Datos,
                                                                Boton_consumirdor_final,
                                                            ])
                                                        ),
                                                        ft.Container(
                                                            width=180,
                                                            height=215,
                                                            padding=0,
                                                            alignment=ft.alignment.bottom_center,
                                                            #sborder=ft.border.all(),
                                                            content=ft.Row(spacing=0,controls=[
                                                                card_totales_generar,
                                                            ])
                                                        ),
                                                        
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Alinear los botones al centro horizontalmente si se desea
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  # Alinear al final del contenedor
                                        ),
                                    )
                                ])
                            ),
                            ft.Container(height=600,content=(
                                ft.Row([ft.VerticalDivider(),])
                            )),
                            ft.Container(width=700,height=600   ,
                                #border=ft.border.all(),
                                content=ft.Column(spacing=0,
                                    controls=[
                                        ft.Row([ft.Text("Ingresa el ID de los productos:",size=25),id_producto,delete_all_button]),ft.Divider(), scrollable_container, 
                                ])
                            ),
                        ])
                    ])             
                ), 
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
                        page_three_ui
                    ]
                )
            )
        ]
    )
