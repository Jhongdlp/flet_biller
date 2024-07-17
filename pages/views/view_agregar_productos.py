import flet as ft
import pymysql

def view_add_pro_all(page: ft.Page):

    page.padding=0
    

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            boton_dark_light_mode.icon = ft.icons.DARK_MODE  # Icono de la luna
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            boton_dark_light_mode.icon = ft.icons.LIGHT_MODE  # Icono de la luna
        page.update()

    def validar_datos(e):
        errores = []
        id_producto = id_producto_texfield.value.strip()
        nombre_producto = nombre_producto_texfield.value.strip()
        tipo_producto = tipo_producto_texfield.value.strip()
        tipo_especifico_producto = tipo_especifico_producto_texfield.value.strip()
        marca_producto = marca_producto_texfield.value.strip()
        proveedor_producto = proveedor_producto_texfield.value.strip()
        iva_producto = iva_producto_texfield.value.strip()
        precio_producto = precio_producto_texfield.value.strip()
        existencias_productos = existencias_productos_texfield.value.strip()
        
        if not all([id_producto, nombre_producto, tipo_producto, marca_producto, proveedor_producto,
                   iva_producto, precio_producto, existencias_productos]):
            errores.append("Por favor, complete todos los campos.")

        if not id_producto.isdigit():
            errores.append("El ID del producto debe ser un número.")

        if any(not c.isalnum() and c not in ' ' for c in nombre_producto):
            errores.append("El nombre del producto solo puede contener letras y números.")

        # Validaciones adicionales para otros campos
        # ...

        # Conexión a la base de datos
        try:
            bd = pymysql.connect(
                host="localhost",
                user="root",
                passwd="",
                db="billify"
            )
            cursor = bd.cursor()
        except Exception as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al conectar a la base de datos: {e}"))
            page.snack_bar.open = True
            page.update()
            return
        # Verificar si el ID ya existe
        cursor.execute("SELECT ID_PROD FROM productos WHERE ID_PROD = %s", (id_producto,))
        if cursor.fetchone():
            errores.append("El ID del producto ya existe en la base de datos.")

        # Si hay errores, mostrarlos
        if errores:
            mensaje_error = "\n".join(errores)
            page.snack_bar = ft.SnackBar(ft.Text(mensaje_error))
            page.snack_bar.open = True
            page.update()
        else:
            # Insertar los datos en la base de datos
            try:
                cursor.execute("""
                    INSERT INTO productos (ID_PROD, NOM_PROD, TIP_PROD, TIP_ESP_PROD, 
                                     MAR_PRO, PROVE_PRO, IVA_PRO, PRE_PRO, EXIS_PRO)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (id_producto, nombre_producto, tipo_producto, tipo_especifico_producto,
                      marca_producto, proveedor_producto, iva_producto, precio_producto,
                      existencias_productos))
                bd.commit()
                page.snack_bar = ft.SnackBar(ft.Text("Producto agregado con éxito."))
                page.snack_bar.open = True
                page.update()
            except Exception as e:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error al agregar producto: {e}"))
                page.snack_bar.open = True
                page.update()
        bd.close()

    def limpiar_campos(e):
        id_producto_texfield.value = ""
        nombre_producto_texfield.value = ""
        tipo_producto_texfield.value = ""
        tipo_especifico_producto_texfield.value = ""
        marca_producto_texfield.value = ""
        proveedor_producto_texfield.value = ""
        iva_producto_texfield.value = ""
        precio_producto_texfield.value = ""
        existencias_productos_texfield.value = ""
        page.update()


    # Crear el botón de cambiar tema
    boton_dark_light_mode = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,  # Icono inicial del sol
        on_click=toggle_theme
    )
    id_producto_texfield=ft.TextField(label=("ID_PRODUCTO"),width=200,height=30)
    nombre_producto_texfield=ft.TextField(label=("nombre del producto"),width=200,height=30)
    tipo_producto_texfield=ft.TextField(label=("Tipo del producto"),width=200,height=30)
    tipo_especifico_producto_texfield=ft.TextField(label=("Tipo especifico del pro"),width=200,height=30)
    marca_producto_texfield=ft.TextField(label=("Marca del producto"),width=200,height=30)
    proveedor_producto_texfield=ft.TextField(label=("Proveedor"),width=200,height=30)
    iva_producto_texfield=ft.TextField(label=("Iva"),width=200,height=30)
    precio_producto_texfield=ft.TextField(label=("Precio"),width=200,height=30)  # Corregido el label
    existencias_productos_texfield=ft.TextField(label=("Existencias"),width=200,height=30)
    def page_home(e):
        page.go("/home")


                   #!Alerta de reportar problema

    def close_Reporte_problemas(e):
        Reporte_problemas.open = False
        page.update()

    def Close_and_open_gracias(e):
        Reporte_problemas.open = False
        page.dialog = Mensaje_de_gracias
        Mensaje_de_gracias.open = True
        page.update()

    def close_dlg_mensaje_gracias(e):
        Mensaje_de_gracias.open = False
        page.update()

    Mensaje_de_gracias = ft.AlertDialog(
        modal=True,
        title=ft.Text("Muchas gracias por tu colaboración!",size=30),
        content=ft.Text("haremos lo posible para solucionarlo",size=15),
        actions=[
            ft.FilledButton("Volver al menu", on_click=close_dlg_mensaje_gracias),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.update()

    Reporte_problemas=ft.AlertDialog(
        modal=True,
        title=ft.Text("Reporte de problemas"),
        content=ft.Text("Por favor selecciona el problema junto a una descripción"),
        actions=[
            ft.Column(
                [
                    ft.Divider(),
                    ft.Checkbox(label="Problema de rendimiento", value=False),
                    ft.Checkbox(label="Error en mostrar datos", value=False),
                    ft.Checkbox(label="Error en el manejo de ventanas", value=False),
                    ft.Checkbox(label="Problemas de bugs", value=False),
                    ft.Checkbox(label="Calculos incorrectos", value=False),
                    ft.Checkbox(label="Otros...", value=False),
                    ft.TextField(
                        label="Describe el problema",
                        multiline=True,
                        max_length=250,
                        max_lines=5,
                    ),
                    ft.Row(
                        [
                            ft.FilledButton(
                                text="Volver",
                                on_click=close_Reporte_problemas,  
                            ),
                            ft.FilledButton(text="Enviar",
                                on_click=Close_and_open_gracias,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
            )
        ],
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    def open_dlg_modal_3(e):
        page.dialog = Reporte_problemas
        Reporte_problemas.open = True
        page.update()

    #!Alerta de cerrar secion
    def close_alert_cerrar_secion(e):
        Alert_cerrar_secion.open = False
        page.update()
    
    def close_alert_and_go_login(e):
        Alert_cerrar_secion.open = False
        page.go("/")
        page.update()

    Alert_cerrar_secion = ft.AlertDialog(
        modal=True,

        title=ft.Text("Por favor confirma"),
        content=ft.Text("Estas seguro de cerrar esta sesión?"),
        actions=[
            ft.TextButton("Si", on_click=close_alert_and_go_login),
            ft.TextButton("No", on_click=close_alert_cerrar_secion),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    
    def open_Alert_cerrar_secion(e):
        page.dialog = Alert_cerrar_secion
        Alert_cerrar_secion.open = True
        page.update()
    view_agregar_productos=ft.Column([
        ft.Container(
            padding=0,
            alignment=ft.alignment.center,
            content=ft.Column(spacing=0,controls=[
                ft.Container(height=60,width=1365,
                    #border=ft.border.all(color='#737780'),  
                    content=ft.Card(
                        elevation=1,
                        margin=5, 
                        variant=ft.CardVariant.OUTLINED,
                        content=ft.Row(spacing=0,controls=[
                            ft.Container(height=60,width=1200,
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    ft.IconButton(icon=ft.icons.ARROW_BACK,
                                        on_click=page_home
                                    ),
                                    ft.VerticalDivider(),
                                    ft.Icon(name=ft.icons.ADD_BUSINESS,size=40),
                                    ft.VerticalDivider(),
                                    ft.Text("Agregar productos",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
                                    ft.VerticalDivider()
                                ])
                            ),
                            ft.Container(height=60,width=1010,
                                content=ft.Row([
                                    ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                    ft.Row([
                                        ft.VerticalDivider(color=ft.colors.TRANSPARENT),
                                        boton_dark_light_mode,
                                        ft.PopupMenuButton(
                                            items=[
                                                ft.PopupMenuItem(),  # divider
                                                ft.PopupMenuItem(
                                                    content=ft.Row(
                                                        [
                                                            ft.Icon(ft.icons.BUG_REPORT),
                                                            ft.Text("Reporte de errores"),
                                                        ]
                                                    ),
                                                    on_click=open_dlg_modal_3
                                                ),
                                                ft.PopupMenuItem(),  # divider
                                                ft.PopupMenuItem(
                                                    content=ft.Row(
                                                        [
                                                            ft.Icon(ft.icons.EXIT_TO_APP),
                                                            ft.Text("Cerrar la sesión"),
                                                        ]
                                                    ),
                                                    on_click=open_Alert_cerrar_secion
                                                ),
                                                ft.PopupMenuItem(),  # divider
                                            ]
                                        )
                                    ],alignment=ft.MainAxisAlignment.END)
                                ])
                            )
                        ]) 
                    )          
                ),
            ])
        ),
        ft.Container(width=1365,height=650,
            alignment=ft.alignment.center,
            content=ft.Row(spacing=0,controls=[
                ft.Container(width=1366,height=650,
                    #border=ft.border.all(),
                    content=(ft.Column([
                        ft.Container(height=10),
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=0,
                            content=ft.Card(
                                elevation=10,
                                content=ft.Column([
                                    ft.Container(
                                        width=450,
                                        padding=20,
                                        alignment=ft.alignment.top_left,
                                        content=ft.Column([
                                            ft.Text("Agrega productos",size=30),
                                            ft.Divider(),
                                            ft.Row([id_producto_texfield,nombre_producto_texfield]),
                                            ft.Divider(color=ft.colors.TRANSPARENT),
                                            ft.Row([tipo_producto_texfield,tipo_especifico_producto_texfield]),
                                            ft.Divider(color=ft.colors.TRANSPARENT),
                                            ft.Row([marca_producto_texfield,proveedor_producto_texfield]),
                                            ft.Divider(color=ft.colors.TRANSPARENT),
                                            ft.Row([iva_producto_texfield,precio_producto_texfield]),
                                            ft.Divider(color=ft.colors.TRANSPARENT),
                                            existencias_productos_texfield,
                                            ft.Divider(color=ft.colors.TRANSPARENT),
                                            ft.Row([
                                                ft.ElevatedButton("Limpiar campos", on_click=limpiar_campos,bgcolor=ft.colors.RED,color=ft.colors.WHITE),
                                                ft.ElevatedButton("Subir nuevo producto", on_click=validar_datos,bgcolor=ft.colors.GREEN,color=ft.colors.WHITE),
                                            ],alignment=ft.MainAxisAlignment.END)

                                        ])
                                        
                                    ),
                                    
                                ])
                            )
                        )
                    ]))
                )
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
                        view_agregar_productos
                    ]
                )
            )
        ]
    )