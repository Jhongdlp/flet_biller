import flet as ft
import bd.base_implemtnacion as bd

def main(page: ft.Page):
    page.title = "Flet DataTable Generator"

    subtotal_value = ft.Text(value="0.00")
    iva_value = ft.Text(value="0.00")
    total_value = ft.Text(value="0.00")
    
    contenedor_de_totales = ft.Container(
        width=200, height=120,
        border=ft.border.all(),
        content=ft.Column([
            ft.Row([ft.Text("Subtotal: "), subtotal_value]),
            ft.Row([ft.Text("Iva: "), iva_value]),
            ft.Row([ft.Text("Total: "), total_value]),
        ])
    )

    id_producto = ft.TextField(label="Agregar Producto (ID)", width=200,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")                           
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
            ft.DataColumn(ft.Text("Acción"), tooltip="Acciones disponibles")
        ],
        rows=[],
    )

    scrollable_container = ft.Container(
        height=400,
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

        product_data = bd.get_product_data(product_id)

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

        cantidad_producto = ft.TextField(value="1", width=65,height=40,
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
            max_length=4                                 
        )

        def validate_cantidad(e):
            if not cantidad_producto.value.isdigit():
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: La cantidad debe ser un número."),duration=2000,
                )
                page.snack_bar.open = True
                id_producto.focus()
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

    delete_all_button = ft.ElevatedButton(text="Eliminar todas las filas", on_click=delete_all_rows)

    page.add(ft.Row([id_producto, contenedor_de_totales]), scrollable_container, delete_all_button)

ft.app(main)
