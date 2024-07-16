import flet as ft
import pymysql
from cryptography.fernet import Fernet

def RegistroPage(page: ft.Page):

    page.window_maximized=True
    page.window_resizable=False
    page.title="Registro"
    #page.window_prevent_close = True
    page.window_title_bar_hidden = True
    page.padding=0

        #!Conectar base de datos
    def minimizar_pagima(e):
        page.window_minimized=True
        page.update()

    def cerrar_login(end):
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Porfavor confirma"),
        content=ft.Text("Estas seguro de cerrar esta aplicacion?"),
        actions=[
            ft.ElevatedButton("Si", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    def highlight_link(e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(e):
        e.control.style.color = None
        e.control.update()

    def highlight_link_registrarse(e):
        e.control.style.color = ft.colors.BLUE_800
        e.control.update()

    def unhighlight_link_registrarse(e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()
    
    def obtener_clave():
        # Conectar a la base de datos MySQL
        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="billify"
        )

        # Crear un cursor para ejecutar consultas en la base de datos
        mcursor = bd.cursor()

        # Consultar la clave en la tabla LLAVE
        sql = "SELECT LLAVE_STR FROM llave"
        mcursor.execute(sql)
        resultado = mcursor.fetchone()
        print(resultado)
        # Cerrar la conexión a la base de datos
        bd.close()
        
        if resultado:
            return resultado[0]  # Devuelve la clave en formato de texto
        else:
            return None


    #!Conectar base de datos
    def Insertar_datos(e):
        # Obtener la clave de la base de datos
        clave_str = obtener_clave()
        
        if clave_str is None:
            print("No se pudo obtener la clave de la base de datos")
            return

        # Crear un objeto Fernet con la clave obtenida de la base de datos
        objeto_cifrado = Fernet(clave_str.encode('utf-8'))
        # Conectar a la base de datos MySQL
        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="billify"
        )

        # Crear un cursor para ejecutar consultas en la base de datos
        mcursor = bd.cursor()

        # Obtener los valores de los campos de entrada
        usuario = Ingrese_usuario.value
        correo_electronico = Correo_electronico.value
        contraseña = Ingrese_contraseña.value
        confirmar_contraseña = Confirmar_contraseña.value
        # Validar que los campos no estén vacíos
        if not usuario or not correo_electronico or not contraseña or not confirmar_contraseña:
            print("Los campos no pueden estar vacíos")
            page.snack_bar = ft.SnackBar(ft.Text(f"Los campos no pueden estar vacíos."))
            page.snack_bar.open = True
            page.update()
            return

        # Validar que la contraseña y la confirmación de la contraseña coincidan
        if contraseña != confirmar_contraseña:
            print("La contraseña y la confirmación de la contraseña no coinciden")
            page.snack_bar = ft.SnackBar(ft.Text(f"La contraseña y la confirmación de la contraseña no coinciden."))
            page.snack_bar.open = True
            page.update()
            return
        
        if contraseña == confirmar_contraseña:
            print("Contraseña correcta")
            
            # Genera una clave en formato de secuencia de bytes:
            texto_encriptado = objeto_cifrado.encrypt(contraseña.encode('utf-8'))
            texto_desencriptado_bytes = objeto_cifrado.decrypt(texto_encriptado)
            print(f"Este es el texto desencriptado en bytes: {texto_desencriptado_bytes}")
            texto_desencriptado = texto_desencriptado_bytes.decode()
            print(f"este e sl texto desincriptado total: {texto_desencriptado}")
        # Crear una consulta SQL para insertar los datos del usuario en la base de datos
        sql = "INSERT INTO registro(USUARIOS,CORREOS,CLAVES) VALUES('{0}', '{1}', '{2}')".format(usuario, correo_electronico, texto_encriptado.decode('utf-8'))

        # Ejecutar la consulta SQL
        try:
            mcursor.execute(sql)
            bd.commit()
            print("Datos insertados correctamente")
            Ingrese_usuario.value = ""
            Correo_electronico.value = ""
            Ingrese_contraseña.value = ""
            Confirmar_contraseña.value = ""
            page.snack_bar = ft.SnackBar(ft.Text(f"Datos insertados correctamente."))
            page.snack_bar.open = True
            page.update()
        except:
            bd.rollback()
            print("Error al insertar datos en la base de datos")
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al insertar datos en la base de datos."))
            page.snack_bar.open = True
            page.update()
        # Cerrar la conexión a la base de datos
        bd.close()

    #!Variables de campos de entrada
    Ingrese_usuario=ft.TextField(label="Usuario", border="underline", hint_text="Ingresa tu usuario",width=250,height=60)
    Correo_electronico=ft.TextField(label="Correo electronico", border="underline", hint_text="Ingresa tu correo electronico",width=250,height=60)
    Ingrese_contraseña=ft.TextField(label="Contraseña", border="underline", 
        hint_text="Ingresa tu contraseña",width=250,height=60,
        password=True, can_reveal_password=True
        )
    Confirmar_contraseña=ft.TextField(label="Confirma tu contraseña", border="underline", 
        hint_text="Ingresa tu contraseña",width=250,height=60,
        password=True, can_reveal_password=True
        )
    
    #!GUI REGISTRO/VENTANA NUEVA
    Registrarse=ft.Container(
        padding=0,
        content=
            ft.Column(
                spacing=10,controls=[
                ft.Divider(color=ft.colors.TRANSPARENT,
                    #height=55
                ),    
                ft.Container(
                    width=1366,
                    padding=0,
                    #border=ft.border.all(),
                    content=ft.Row([
                        ft.Card(
                            width=650,
                            height=500,
                            elevation=10,
                            variant=ft.CardVariant.OUTLINED,
                            #border=ft.border.all(),
                            content=ft.Row(
                                spacing=0,controls=[
                                ft.Card(
                                    #padding=0,
                                    width=325,
                                    height=600,
                                    #border=ft.border.all(),
                                    content=ft.Image(
                                        src=f"https://i.ibb.co/93KG58q/fondo-register-empresa.jpg",
                                        fit=ft.ImageFit.FILL,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    )
                                ),
                                ft.Container(
                                    padding=0,
                                    height=500,
                                    width=325,
                                    #border=ft.border.all(),
                                    content=ft.Row(spacing=0,controls=[
                                            ft.Column([
                                                ft.Container(
                                                    width=325,
                                                    content=(ft.Row(spacing=0,controls=[
                                                        ft.Container(width=325,height=40,
                                                            #border=ft.border.all(),
                                                            content=(ft.Row([
                                                                ft.Text("Registro",size=26,weight=ft.FontWeight.W_900,color='#3d5ff5')
                                                            ],alignment=ft.MainAxisAlignment.CENTER)
                                                            )           
                                                        )
                                                    ],alignment=ft.MainAxisAlignment.CENTER))
                                                ),
                                                ft.Container(
                                                    padding=0,
                                                    #height=30,
                                                    width=325,
                                                    #border=ft.border.all(),
                                                    content=ft.Row(spacing=0,controls=[ft.Text("Crea una cuenta para acceder a la\n           facturación electrónica.",
                                                            size=14)],
                                                        alignment=ft.MainAxisAlignment.CENTER)
                                                ), 
                                                ft.Container(
                                                    width=310,
                                                    content=ft.Divider(height=2)),
                                                ft.Container(
                                                    padding=10,
                                                    #height=200,
                                                    width=325,
                                                    alignment = ft.alignment.center,
                                                    #alignment=ft.MainAxisAlignment.CENTER,
                                                    #border=ft.border.all(),
                                                    content=ft.Row([
                                                        ft.Column([
                                                            Ingrese_usuario,
                                                            Correo_electronico,
                                                            Ingrese_contraseña,
                                                            Confirmar_contraseña
                                                            
                                                        ])
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                ), 
                                                ft.Container(
                                                    width=325,
                                                    #border=ft.border.all(),
                                                    content=ft.Row([
                                                        ft.ElevatedButton(
                                                            #"Iniciar",
                                                            on_click=Insertar_datos,
                                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5,)),
                                                            width=250,
                                                            height=35,
                                                            bgcolor=ft.colors.GREEN_500,
                                                            color=ft.colors.WHITE,
                                                            content=ft.Text("Registrarse",size=23)
                                                        )
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                ),
                                                ft.Container(
                                                    width=325,
                                                    content=(
                                                        ft.Row(spacing=0,controls=[
                                                            ft.Column([
                                                                ft.Text(
                                                                    disabled=False,
                                                                    spans=[
                                                                        ft.TextSpan("¿Ya tienes una cuenta?"),
                                                                        ft.TextSpan(
                                                                            "Iniciar secion",
                                                                            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE,color=ft.colors.BLUE),
                                                                            on_click=lambda _: page.go("/"),
                                                                            on_enter=highlight_link_registrarse,
                                                                            on_exit=unhighlight_link_registrarse,

                    
                                                                        ),
                                                                    ],size=12
                                                                ),
                                                            ])
                                                            
                                                        ],alignment=ft.MainAxisAlignment.CENTER)
                                                    )
                                                ),
                                                ft.Divider(height=30),
                                            ])
                                        ])
                                    )
                                ]),
                        ),
                    ],alignment=ft.MainAxisAlignment.CENTER)
                )
            ])
    )
    return ft.Row(
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        Registrarse
                    ]
                )
            )
        ]
    )
