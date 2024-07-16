import flet as ft
import re

from logic.validaciones import validar_cedula_ecuador,validar_pasaporte_ecuador,validar_ruc_ecuador
from components.rail import create_navigation_rail
from sql.base_implemtnacion import get_product_data
from datetime import datetime
from xml.dom import minidom

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image

import os
import uuid

import pymysql
import xml.etree.ElementTree as ET



def generar_factura_pro(page: ft.Page):
    #!==================================================================================
    #!=                                                                                =
    #!=                                 PAGINA TRES                                     =
    #!=                                                                                =
    #!==================================================================================    
    # Inicializar el color de fondo del contenedor y el modo de la página
    #page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=0
    page.title="Historia de facturas"
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

    identificador_cliente_texfield=ft.TextField(label=("Identificador"),width=230,height=45,
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

    Escoger_identificador=ft.Dropdown(
        width=100,
        height=35,
        content_padding=1,
        options=[
            ft.dropdown.Option("Cedula"),
            ft.dropdown.Option("RUC"),
            ft.dropdown.Option("Pasaporte"),
        ],  
        value="Cedula"   
    )

    subtotal_value = ft.Text(value="0.00")
    iva_value = ft.Text(value="0.00")
    total_value = ft.Text(value="0.00",weight=ft.FontWeight.W_900)

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



   
    
    def generar_factura_pdf(e):
        """Genera un PDF con la estructura de una factura."""

        # --- Datos de la empresa ---
        nombre_empresa = "Super Compra Inc."
        direccion_empresa = "Cacha y Jose Andrango 123, Quito"
        telefono_empresa = "+593-098-3853-500"
        email_empresa = "supercompra@gruposuper.com"
        logo_path = "src/Logo.png"  # Añadir la ruta a tu logotipo

        # --- Obtener datos del cliente ---
        tipo_id = Escoger_identificador.value
        if tipo_id == "Cedula":
            identificador_cliente = f"C.{identificador_cliente_texfield.value}"
            if not validar_cedula_ecuador(identificador_cliente_texfield.value):
                page.snack_bar = ft.SnackBar(ft.Text("Cédula inválida"))
                page.snack_bar.open = True
                page.update()
                return
        elif tipo_id == "RUC":
            identificador_cliente = f"R.{identificador_cliente_texfield.value}"
            if not validar_ruc_ecuador(identificador_cliente_texfield.value):
                page.snack_bar = ft.SnackBar(ft.Text("RUC inválido"))
                page.snack_bar.open = True
                page.update()
                return
        elif tipo_id == "Pasaporte":
            identificador_cliente = f"P.{identificador_cliente_texfield.value}"
            if not validar_pasaporte_ecuador(identificador_cliente_texfield.value):
                page.snack_bar = ft.SnackBar(ft.Text("Pasaporte inválido"))
                page.snack_bar.open = True
                page.update()
                return
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Tipo de ID inválido"))
            page.snack_bar.open = True
            page.update()
            return

        nombre_cliente = nombre_cliente_texfield.value + " " + apellido_cliente_texfield.value
        direccion_cliente = direccion_cliente_texfield.value

        # --- Generar código único para la factura ---
        codigo_factura = str(uuid.uuid4())

        # --- Obtener fecha y hora actual ---
        fecha_emision = datetime.now().strftime("%Y-%m-%d")

        # --- Crear carpeta "facturas" si no existe ---
        if not os.path.exists("facturas"):
            os.makedirs("facturas")

        # --- Crear el documento PDF ---
        nombre_archivo = os.path.join("facturas", f"factura_{codigo_factura}.pdf")
        doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
        elements = []

        # --- Estilos ---
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='FacturaTitle', fontSize=20, alignment=1, spaceAfter=12, leading=24))  # Título centrado
        styles.add(ParagraphStyle(name='RightAlign', alignment=2, leading=14))  # Alineación a la derecha

        # --- Logotipo de la empresa ---
        if os.path.exists(logo_path):
            logo = Image(logo_path, width=70, height=50)
            elements.append(logo)

        # --- Encabezado de la factura ---
        elements.append(Paragraph(f"{nombre_empresa}", styles['FacturaTitle']))
        elements.append(Paragraph(f"Dirección: {direccion_empresa}", styles['Normal']))
        elements.append(Paragraph(f"Teléfono: {telefono_empresa}", styles['Normal']))
        elements.append(Paragraph(f"Email: {email_empresa}", styles['Normal']))
        elements.append(Spacer(1, 24))

        # --- Información del cliente ---
        elements.append(Paragraph("Factura a:", styles['Heading2']))
        elements.append(Paragraph(f"Nombre: {nombre_cliente}", styles['Normal']))
        elements.append(Paragraph(f"Identificación: {identificador_cliente}", styles['Normal']))
        elements.append(Paragraph(f"Dirección: {direccion_cliente}", styles['Normal']))
        elements.append(Spacer(1, 24))

        # --- Detalles de la factura ---
        elements.append(Paragraph(f"Factura No: {codigo_factura}", styles['Normal']))
        elements.append(Paragraph(f"Fecha: {fecha_emision}", styles['Normal']))
        elements.append(Spacer(1, 24))

        # --- Tabla de productos ---
        data = [["No.", "Descripción", "Cantidad", "Precio Unitario", "Total"]]
        for i, row in enumerate(data_table.rows):
            cantidad = float(row.cells[6].content.value)
            precio = float(row.cells[5].content.value)
            total = cantidad * precio
            data.append([
                i + 1,
                row.cells[2].content.value,
                cantidad,
                f"{precio:.2f}",  # Formatear precio a 2 decimales
                f"{total:.2f}"  # Formatear total a 2 decimales
            ])

        table = Table(data, colWidths=[30, 250, 60, 90, 90])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        elements.append(table)
        elements.append(Spacer(1, 24))

        # --- Totales en tabla ---
        total_data = [
            ["", "Subtotal:", f"{subtotal_value.value}"],
            ["", "IVA:", f"{iva_value.value}"],
            ["", "Total:", f"{total_value.value}"]
        ]

        total_table = Table(total_data, colWidths=[400, 100, 90])
        total_table.setStyle(TableStyle([
            ('BACKGROUND', (1, 0), (2, 0), colors.beige),
            ('TEXTCOLOR', (1, 0), (2, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(total_table)
        elements.append(Spacer(1, 24))

        # ---  Mensaje final ---
        elements.append(Paragraph("¡Gracias por su compra!", styles['Normal']))

        # --- Generar el PDF ---
        doc.build(elements)

    def generar_factura_xml(e):
        # --- Generar código único para la factura ---
        codigo_factura = str(uuid.uuid4())  # Usando UUID para un ID único

        # --- Obtener fecha y hora actual ---
        fecha_emision = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        # Crear el elemento raíz del XML
        factura = ET.Element("Factura")
        factura.set("xmlns", "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2")
        factura.set("xmlns:cac", "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2")
        factura.set("xmlns:cbc", "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2")

        # --- Agregar ID único y fecha de emisión a la factura ---
        id_factura = ET.SubElement(factura, "cbc:ID")
        id_factura.text = codigo_factura

        fecha = ET.SubElement(factura, "cbc:IssueDate")
        fecha.text = fecha_emision

        # --- Información del emisor ---
        emisor = ET.SubElement(factura, "cbc:AccountingSupplierParty")
        party = ET.SubElement(emisor, "cac:Party")
        nombre_emisor = ET.SubElement(party, "cac:PartyName")
        nombre_emisor.text = "Jhon Guadalupe"
        # ... (Agregar más información del emisor si es necesario)

        # --- Información del cliente ---
        receptor = ET.SubElement(factura, "cbc:AccountingCustomerParty")
        party_receptor = ET.SubElement(receptor, "cac:Party")
        nombre_receptor = ET.SubElement(party_receptor, "cac:PartyName")
        nombre_receptor.text = nombre_cliente_texfield.value + " " + apellido_cliente_texfield.value
        # ... (Agregar más información del cliente si es necesario)

        # --- Líneas de la factura (productos) ---
        for i, row in enumerate(data_table.rows):
            linea_factura = ET.SubElement(factura, "cac:InvoiceLine", {"ID": str(i + 1)})

            cantidad = ET.SubElement(linea_factura, "cbc:InvoicedQuantity")
            cantidad.text = str(row.cells[6].content.value)  # Convertir a str

            descripcion = ET.SubElement(linea_factura, "cbc:Description")
            descripcion.text = row.cells[2].content.value

            precio_unitario = ET.SubElement(linea_factura, "cac:Price")
            precio_unitario.text = str(row.cells[5].content.value)  # Convertir a str

        # --- Firma electrónica (simulada) ---
        firma = ET.SubElement(factura, "FirmaElectronica")
        firma.text = """-----BEGIN PKCS7-----
    MIIGywYJKoZIhvcNAQcCoIIGszCCBrMCAQExCzAJBgkqhkiG9w0B
    QIhFw0nYW1wbGUgQ29ycG9yYXRpb24xCzAJBgNVBAYTAlVTMQsw
    CQYDVQQDDAJUZXN0MRUwEwYDVQQKDAxTeXN0dGVtcyBDbzCCASIw
    DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANx/xxxxx/xxxxx
    /xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx
    /xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx
    /xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx
    /xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx
    /xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx
    -----END PKCS7-----""" 

        # --- Convertir el XML a cadena con formato ---
        xml_str = ET.tostring(factura, encoding="unicode")
        xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")

        print(xml_str)  # Imprimir el XML en la consola
        # --- Crear carpeta "facturas" si no existe ---
        if not os.path.exists("facturas"):
            os.makedirs("facturas")

        # --- Guardar el XML en la carpeta "facturas" ---
        nombre_archivo = os.path.join("facturas", f"factura_{codigo_factura}.xml")
        with open(nombre_archivo, "w") as f:
            f.write(xml_str)

    def guardar_factura_db(e):
        """Guarda los datos de la factura en la base de datos."""

        # 1. Obtener datos de la factura (incluyendo teléfono y email)
        nombre_cliente = nombre_cliente_texfield.value
        apellido_cliente = apellido_cliente_texfield.value
        telefono_cliente = telefono_cliente_texfield.value
        email_cliente = mail_cliente_texfield.value
        fecha_factura = datetime.now().strftime("%Y-%m-%d")

        # --- Obtener el identificador con el formato correcto ---
        tipo_id = Escoger_identificador.value
        if tipo_id == "Cedula":
            identificador_cliente = f"C.{identificador_cliente_texfield.value}"
            if not validar_cedula_ecuador(identificador_cliente_texfield.value):
                # Manejar error de cédula inválida
                print("Cédula inválida")
                page.snack_bar = ft.SnackBar(ft.Text("Cédula inválida"))
                page.snack_bar.open = True
                page.update()
                return  
        elif tipo_id == "RUC":
            identificador_cliente = f"R.{identificador_cliente_texfield.value}"
            if not validar_ruc_ecuador(identificador_cliente_texfield.value):
                # Manejar error de RUC inválido
                print("RUC inválido")
                page.snack_bar = ft.SnackBar(ft.Text("RUC inválido"))
                page.snack_bar.open = True
                page.update()
                return
        elif tipo_id == "Pasaporte":
            identificador_cliente = f"P.{identificador_cliente_texfield.value}"
            if not validar_pasaporte_ecuador(identificador_cliente_texfield.value):
                # Manejar error de pasaporte inválido
                print("Pasaporte inválido")
                page.snack_bar = ft.SnackBar(ft.Text("Pasaporte inválido"))
                page.snack_bar.open = True
                page.update()
                return 
        else:
            # Manejar error de tipo de ID no válido
            print("Tipo de ID inválido")
            page.snack_bar = ft.SnackBar(ft.Text("Tipo de ID inválido"))
            page.snack_bar.open = True
            page.update()
            return


        # 2. Construir la cadena de productos
        productos_str = ",".join(
            [
                f"{row.cells[1].content.value}.{row.cells[6].content.value}"
                for row in data_table.rows
            ]
        )

        # 3. Construir la cadena de totales
        totales_str = f"{subtotal_value.value},{iva_value.value},{total_value.value}"

        # 4. Conexión a la base de datos 
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="billify"
        )

        try:
            # 5. Crear un cursor
            cursor = conexion.cursor()

            # 6. Consulta SQL para insertar la factura 
            sql = """
                INSERT INTO facturas (identificador, nombre, apellido, telefono, 
                                    email, fecha, productos, totales) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                identificador_cliente, # Usamos el identificador validado
                nombre_cliente,
                apellido_cliente,
                telefono_cliente,  
                email_cliente,     
                fecha_factura,
                productos_str,
                totales_str,
            )

            # 7. Ejecutar la consulta
            cursor.execute(sql, valores)

            # 8. Hacer commit para guardar los cambios
            conexion.commit()
        except Exception as e:
            print(f"Error al guardar la factura: {e}")

            page.snack_bar = ft.SnackBar(
                ft.Text("Error al guardar la factura.", size=20),
                bgcolor=ft.colors.RED_400,
                duration=3000,
            )
            page.snack_bar.open = True
            page.update()

        finally:
            # 9. Cerrar el cursor y la conexión
            cursor.close()
            conexion.close()
    
    
    def eliminar_todo(e):
        delete_all_rows(e)
        identificador_cliente_texfield.value=""
        nombre_cliente_texfield.value=""
        apellido_cliente_texfield.value=""
        direccion_cliente_texfield.value=""
        telefono_cliente_texfield.value=""
        mail_cliente_texfield.value=""
        identificador_cliente_texfield.read_only=False
        nombre_cliente_texfield.read_only=False
        apellido_cliente_texfield.read_only=False
        direccion_cliente_texfield.read_only=False
        telefono_cliente_texfield.read_only=False
        mail_cliente_texfield.read_only=False
        on_change(e)
        page.update()
    
    def limpiar_datos_clientes(e):
        identificador_cliente_texfield.value=""
        nombre_cliente_texfield.value=""
        apellido_cliente_texfield.value=""
        direccion_cliente_texfield.value=""
        telefono_cliente_texfield.value=""
        mail_cliente_texfield.value=""
        identificador_cliente_texfield.read_only=False
        nombre_cliente_texfield.read_only=False
        apellido_cliente_texfield.read_only=False
        direccion_cliente_texfield.read_only=False
        telefono_cliente_texfield.read_only=False
        mail_cliente_texfield.read_only=False
        on_change(e)
        page.update()

    def consumidor_final(e):
        identificador_cliente_texfield.value="0000000000"
        nombre_cliente_texfield.value="**************"
        apellido_cliente_texfield.value="**************"
        direccion_cliente_texfield.value="*****************"
        telefono_cliente_texfield.value="0000000000"
        mail_cliente_texfield.value="consumidorfinal@consumidorfinal.com"
        identificador_cliente_texfield.read_only=True
        nombre_cliente_texfield.read_only=True
        apellido_cliente_texfield.read_only=True
        direccion_cliente_texfield.read_only=True
        telefono_cliente_texfield.read_only=True
        mail_cliente_texfield.read_only=True
        on_change(e)
        page.update()


    def llamar_a_todas_las_funciones(e):
        generar_factura_xml(e)
        generar_factura_pdf(e)
        guardar_factura_db(e)
        page.update()


    # Crear los controles del AlertDialog
    dinero_input = ft.TextField(label="Dinero Ingresado", on_change=lambda e: (calcular_cambio(e), limpiar_error(e)))
    cambio_text = ft.Text("Cambio: 0.00",weight=ft.FontWeight.W_900,size=20)
    total_productos_text = ft.Text(f"Total de productos: {len(data_table.rows)}")
    def cerrar_alert_metodo_de_pago(e):
        dlg.open = False
        page.update()
        page.snack_bar = ft.SnackBar(
                ft.Text("Factura guardada correctamente.", size=20),
                bgcolor=ft.colors.GREEN_400, 
                duration=3000,
            )
        page.snack_bar.open = True
        dinero_input.value=""

        page.update()


    def calcular_cambio(e):
        """Calcula el cambio cuando cambia el valor de 'dinero_input'."""
        try:
            dinero_ingresado = float(dinero_input.value)
            cambio = dinero_ingresado - float(total_value.value)
            cambio_text.value = f"Cambio: {cambio:.2f}"
            page.update()
        except ValueError:
            cambio_text.value = "Ingresa un número válido"
            page.update()
        page.update()

    def generar_factura_boton(e):
        try:
            dinero_ingresado = float(dinero_input.value)
            cambio = dinero_ingresado - float(total_value.value)
            if dinero_input.value == "":
                dinero_input.error_text = "Este campo no puede estar vacío"
                page.update()
                return
            if cambio < 0:
                cambio_text.value = "El cambio no puede ser negativo"
                page.update()
                return
            # Aquí agregas la lógica para generar la factura
            cambio_text.value = f"Factura generada con cambio: {cambio:.2f}"
            llamar_a_todas_las_funciones(e)
            page.update()
            eliminar_todo(e)
            page.update()
            cerrar_alert_metodo_de_pago(e)
            page.update()
        except ValueError:
            dinero_input.error_text = "Ingresa un número válido"
        page.update()
    page.update()
    def limpiar_error(e):
        if dinero_input.error_text:
            dinero_input.error_text = ""
            page.update()
    page.update()

        
        # Crear el AlertDialog
    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Efectua el pago: ",weight=ft.FontWeight.W_900),
        content=ft.Container(
            height=300,
            content=ft.Column(
            [
                ft.Divider(),
                ft.Column(spacing=0, controls=[
                    ft.Row([ft.Text("Subtotal: "), subtotal_value]),
                    ft.Row([ft.Text("Iva: "), iva_value]),
                    ft.Row([ft.Text("Total: ",weight=ft.FontWeight.W_900), total_value]),
                    ft.Divider(color=ft.colors.TRANSPARENT),
                ]),
                dinero_input,
                ft.Divider(),
                cambio_text,
                total_productos_text,
            ])
        ),
        actions=[
            ft.ElevatedButton(
                text="Generar Factura",
                on_click=generar_factura_boton
            ),
            ft.ElevatedButton(
                text="Cerrar",
                on_click=cerrar_alert_metodo_de_pago
            ),
        ],
    )
    page.update()

    def abrir_dialogo_pago(e):
        """Abre el AlertDialog para gestionar el pago."""
        alert_metodo_pago.open = False
        page.update()
        page.dialog = dlg
        dlg.open = True
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

    
    def on_generar_factura_click(e):
        """
        Valida los campos y genera la factura XML y PDF si todo es correcto.
        """

        # Validar campos de cliente
        error = False  # Variable para controlar si hay algún error en la validación
        if not identificador_cliente_texfield.value:
            identificador_cliente_texfield.error_text = "Este campo es obligatorio"
            identificador_cliente_texfield.error_style = ft.TextStyle(color=ft.colors.RED)
            error = True
        else:
            identificador_cliente_texfield.error_text = None  # Limpiar error si se corrige

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

    # --- Validar el identificador del cliente ---
        tipo_id = Escoger_identificador.value
        if tipo_id == "Cedula":
            if not validar_cedula_ecuador(identificador_cliente_texfield.value):
                identificador_cliente_texfield.error_text = "Cédula inválida"
                page.update()
                return
        elif tipo_id == "RUC":
            if not validar_ruc_ecuador(identificador_cliente_texfield.value):
                identificador_cliente_texfield.error_text = "RUC inválido"
                page.update()
                return
        elif tipo_id == "Pasaporte":
            if not validar_pasaporte_ecuador(identificador_cliente_texfield.value):
                identificador_cliente_texfield.error_text = "Pasaporte inválido"
                page.update()
                return
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Tipo de ID inválido"))
            page.snack_bar.open = True
            page.update()
            return

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
            abrir_alert_metodo_pago(e)
            page.update()

    def on_change(e):
        if identificador_cliente_texfield.error_text:
            identificador_cliente_texfield.error_text = None
            identificador_cliente_texfield.update()

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
    identificador_cliente_texfield.on_change = on_change
    nombre_cliente_texfield.on_change = on_change
    apellido_cliente_texfield.on_change = on_change
    direccion_cliente_texfield.on_change = on_change
    telefono_cliente_texfield.on_change = on_change
    mail_cliente_texfield.on_change = on_change
    page.update()
    delete_all_button = ft.ElevatedButton(text="Limpiar todas las filas", on_click=delete_all_rows,color=ft.colors.WHITE,bgcolor=ft.colors.RED)

    Boton_consumirdor_final=ft.ElevatedButton("Consumidor final",width=158,height=35,bgcolor=ft.colors.GREEN_500,color="WHITE",
        on_click=consumidor_final
        )
    Boton_Eliminar_Datos=ft.ElevatedButton("Eliminar Datos",width=147,height=35,bgcolor=ft.colors.RED,color=ft.colors.WHITE,
        on_click=eliminar_todo
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
            on_click=on_generar_factura_click
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
                                    ft.Row(spacing=0,controls=[
                                        ft.Text("Datos de cliente",size=25),
                                        ft.ElevatedButton(text="Limpiar",on_click=limpiar_datos_clientes,bgcolor=ft.colors.RED,color=ft.colors.WHITE),
                                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                    ft.Divider(),
                                        ft.Row(spacing=5,controls=[
                                            Escoger_identificador,
                                            identificador_cliente_texfield,

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
                                                            height=150,
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
                                                            height=150,
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
