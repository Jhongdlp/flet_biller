import flet as ft
from sql.base_implemtnacion import get_product_data
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.dom import minidom
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import uuid
import os
import pymysql
def main(page: ft.Page):
    page.title = "Flet DataTable Generator"

    # --- Campos para datos del cliente ---
    cedula = ft.TextField(label="Cédula", width=200)
    nombre = ft.TextField(label="Nombre", width=200)
    direccion = ft.TextField(label="Dirección", width=200)
    apellido = ft.TextField(label="Apellido", width=200)
    telefono = ft.TextField(label="Teléfono", width=200)
    email = ft.TextField(label="E-mail", width=200)

    # --- Campos para totales ---
    subtotal_value = ft.Text(value="0.00")
    iva_value = ft.Text(value="0.00")
    total_value = ft.Text(value="0.00")

    contenedor_de_totales = ft.Container(
        width=200,
        height=120,
        border=ft.border.all(),
        content=ft.Column(
            [
                ft.Row([ft.Text("Subtotal: "), subtotal_value]),
                ft.Row([ft.Text("Iva: "), iva_value]),
                ft.Row([ft.Text("Total: "), total_value]),
            ]
        ),
    )

    id_producto = ft.TextField(
        label="Agregar Producto (ID)",
        width=200,
        input_filter=ft.InputFilter(
            allow=True, regex_string=r"[0-9]", replacement_string=""
        ),
    )

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
            ft.DataColumn(ft.Text("Acción"), tooltip="Acciones disponibles"),
        ],
        rows=[],
    )

    scrollable_container = ft.Container(
        height=300, content=ft.Column([data_table], scroll=ft.ScrollMode.AUTO)
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
        iva = subtotal * 0.15
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
                ft.Text(
                    f"Error: El producto con ID {product_id} no se encontró en la base de datos.",
                    size=20,
                ),
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
                    ft.Text(
                        f"El producto con ID {product_data[0]} ya ha sido  agregado.",
                        size=20,
                        color=ft.colors.WHITE,
                    ),
                    bgcolor=ft.colors.BLUE_800,
                    duration=2000,
                    show_close_icon=True,
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

        cantidad_producto = ft.TextField(
            value="1",
            width=65,
            height=40,
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"[0-9]", replacement_string=""
            ),
            max_length=4,
        )

        def validate_cantidad(e):
            if not cantidad_producto.value.isdigit():
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser un número."),
                    duration=2000,
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

            cantidad = int(cantidad_producto.value)
            existencias = product_data[5]

            if cantidad <= 0:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser mayor que cero."),
                    duration=2000,
                )
                page.snack_bar.open = True
                id_producto.focus()
                page.update()
                return

            if cantidad > existencias:
                page.snack_bar = ft.SnackBar(
                    ft.Text(
                        f"Error: La cantidad ingresada {cantidad} excede las existencias disponibles {existencias} para el producto {product_data[1]} (ID: {product_data[0]}).",
                        duration=2000,
                    ),
                )
                page.snack_bar.open = True
                page.update()
                return

            calculate_subtotal()

        cantidad_producto.on_change = validate_cantidad

        new_row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows) + 1))),
                ft.DataCell(ft.Text(product_data[0])),
                ft.DataCell(ft.Text(product_data[1])),
                ft.DataCell(ft.Text(product_data[2])),
                ft.DataCell(ft.Text(product_data[3])),
                ft.DataCell(ft.Text(product_data[4])),
                ft.DataCell(cantidad_producto),
                ft.DataCell(
                    ft.IconButton(
                        icon=ft.icons.DELETE_FOREVER,
                        tooltip="Eliminar producto",
                        on_click=lambda e: delete_product(e, new_row),
                    )
                ),
            ]
        )
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

    delete_all_button = ft.ElevatedButton(
        text="Eliminar todas las filas", on_click=delete_all_rows
    )

    def generar_factura_pdf(e):
        """Genera un PDF con la estructura de una factura."""

        # --- Datos de la empresa ---
        nombre_empresa = "Tech Solutions Inc."
        direccion_empresa = "Calle Falsa 123, Ciudad"
        telefono_empresa = "+1-555-123-4567"
        email_empresa = "info@techsolutions.com"

        # --- Obtener datos del cliente ---
        nombre_cliente = nombre.value + " " + apellido.value
        cedula_cliente = cedula.value
        direccion_cliente = direccion.value
        # ... (Obtener otros datos del cliente)

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
        styles.add(ParagraphStyle(name='FacturaTitle', fontSize=18, alignment=1))  # Título centrado
        styles.add(ParagraphStyle(name='RightAlign', alignment=2))  # Alineación a la derecha

        # --- Encabezado de la factura ---
        elements.append(Paragraph(f"{nombre_empresa}", styles['FacturaTitle']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Dirección: {direccion_empresa}", styles['Normal']))
        elements.append(Paragraph(f"Teléfono: {telefono_empresa}", styles['Normal']))
        elements.append(Paragraph(f"Email: {email_empresa}", styles['Normal']))
        elements.append(Spacer(1, 24))

        # --- Información del cliente ---
        elements.append(Paragraph("Factura a:", styles['Heading2']))
        elements.append(Paragraph(f"Nombre: {nombre_cliente}", styles['Normal']))
        elements.append(Paragraph(f"Cédula: {cedula_cliente}", styles['Normal']))
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

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        elements.append(Spacer(1, 24))

        # --- Totales ---
        elements.append(Paragraph("Subtotal:", styles['RightAlign']))
        elements.append(Paragraph(f"{subtotal_value.value}", styles['RightAlign']))
        elements.append(Paragraph("IVA:", styles['RightAlign']))
        elements.append(Paragraph(f"{iva_value.value}", styles['RightAlign']))
        elements.append(Paragraph("Total:", styles['RightAlign']))
        elements.append(Paragraph(f"{total_value.value}", styles['RightAlign']))

        # ---  Mensaje final --- 
        elements.append(Spacer(1, 24))
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
        nombre_receptor.text = nombre.value + " " + apellido.value
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
        cedula_cliente = cedula.value
        nombre_cliente = nombre.value
        apellido_cliente = apellido.value
        telefono_cliente = telefono.value
        email_cliente = email.value
        fecha_factura = datetime.now().strftime("%Y-%m-%d")

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

            # 6. Consulta SQL para insertar la factura (incluyendo teléfono y email)
            sql = """
                INSERT INTO facturas (cedula, nombre, apellido, telefono, 
                                    email, fecha, productos, totales) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                cedula_cliente,
                nombre_cliente,
                apellido_cliente,
                telefono_cliente,  # Nuevo campo
                email_cliente,     # Nuevo campo
                fecha_factura,
                productos_str,
                totales_str,
            )

            # 7. Ejecutar la consulta
            cursor.execute(sql, valores)

            # 8. Hacer commit para guardar los cambios
            conexion.commit()

            page.snack_bar = ft.SnackBar(
                ft.Text("Factura guardada correctamente.", size=20),
                bgcolor=ft.colors.GREEN_400, 
                duration=3000,
            )
            page.snack_bar.open = True
            page.update()

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
        
    guardar_db_button = ft.ElevatedButton(
        text="Guardar Factura en BD", on_click=guardar_factura_db
    )
    
    def generar_factura(e):
        """Genera la factura XML y el PDF solo si hay productos."""

        if data_table.rows:  # Verificar si hay filas en la tabla
            generar_factura_xml(e)
            generar_factura_pdf(e)
            guardar_factura_db(e)
        else:
            # Mostrar un mensaje de error o alerta
            page.snack_bar = ft.SnackBar(
                ft.Text("No hay productos en la factura.", size=20),
                bgcolor=ft.colors.RED_400,
                duration=3000  # Mostrar por 3 segundos
            )
            page.snack_bar.open = True
            page.update()
            
    generar_factura_button = ft.ElevatedButton(
        text="Generar Factura XML", on_click=generar_factura
    )
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
        # --- Agregar los nuevos elementos a la página ---
    def generar_pago(e):
        generar_factura_pdf
        generar_factura_xml
        guardar_factura_db
    boton_pago = ft.ElevatedButton(text="Procesar Pago", on_click=generar_pago)
    page.add(
        ft.Column(
            [
                ft.Row([cedula,
                nombre,
                direccion,boton_pago,
                apellido,]),
                generar_factura_button,
                guardar_db_button,
                telefono,
                email,
                ft.Row([id_producto, contenedor_de_totales]),
                scrollable_container,
                delete_all_button,
            
            ]
        )
    )


ft.app(main)