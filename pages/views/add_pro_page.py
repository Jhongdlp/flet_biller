import flet as ft
from components.rail import create_navigation_rail
from sql.base_implemtnacion import get_product_data

def generar_factura_pro(page: ft.Page):
    #!==================================================================================
    #!=                                                                                =
    #!=                                 PAGINA TRES                                     =
    #!=                                                                                =
    #!==================================================================================    
    subtotal_value = ft.Text(value="0.00")
    iva_value = ft.Text(value="0.00")
    total_value = ft.Text(value="0.00")
    
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
            #on_click=open_dlg_generar_factura
            ),
            ft.Divider(color=ft.colors.TRANSPARENT),
        ])
    ))


    id_producto = ft.TextField(width=150,height=30,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        content_padding=5                          
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
        height=300,
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

    delete_all_button = ft.ElevatedButton(text="Eliminar todas las filas", on_click=delete_all_rows)

    Boton_consumirdor_final=ft.ElevatedButton("Consumidor final",width=158,height=35,bgcolor=ft.colors.GREEN_500,color="WHITE",
        #on_click=Boton_Consumidor_final_logica
        )
    Boton_Eliminar_Datos=ft.ElevatedButton("Eliminar Datos",width=147,height=35,bgcolor=ft.colors.RED,color=ft.colors.WHITE,
        #on_click=Boton_Eliminar_Datos_logica
        )
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
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=320,
                                #border=ft.border.only(right=ft.border.BorderSide(1, "#737780")),
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    ft.TextField(
                                        height=35,
                                        #label="My favorite color",
                                        hint_text="Buscar",
                                        #helper_text="You can type only one color",
                                        #counter_text="0 symbols typed",
                                        prefix_icon=ft.icons.SEARCH_OUTLINED,
                                    ),
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=145,height=650,
                    #border=ft.border.all(),
                    content=( create_navigation_rail(page, selected_index=2))
                ),
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
                                        ft.TextField(label=("Cedula"),width=230,height=35.),
                                        ft.IconButton(icon=ft.icons.DOCUMENT_SCANNER),
                                        ft.IconButton(icon=ft.icons.DOCK)
                                    ]),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("Nombre"),width=230,height=35),
                                        ft.VerticalDivider(),
                                        ft.TextField(label=("Apellido"),width=230,height=35),
                                    ]),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("Direccion"),width=230,height=35),
                                        ft.VerticalDivider(),
                                        ft.TextField(label=("Telefono"),width=230,height=35),
                                    ]),
                                    ft.Divider(),
                                    ft.Row(spacing=0,controls=[
                                        ft.TextField(label=("E-Mail"),width=475,height=35),
                                        
                                    ]),
                                    ft.Divider(),
                                    ft.Container(width=500,
                                        content=ft.Column(controls=[
                                            ft.Row([
                                                Boton_Eliminar_Datos,
                                                Boton_consumirdor_final,
                                                card_totales_generar,
                                            ])
                                        ])
                                    ),
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
