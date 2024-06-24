import flet as ft
from flet_route import Params,Basket
import pymysql
from cryptography.fernet import Fernet

def Login(page: ft.Page,params: Params, basket: Basket):
    page.window_maximized=True
    #page.window_resizable=False
    #page.window_prevent_close = True
    page.window_title_bar_hidden = True
    page.padding=0
    page.update()
    #!Obtiene=la=clave=de=la=bd======================================================
    def obtener_clave():
        # Conectar a la base de datos MySQL
        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="Billify"
        )

        # Crear un cursor para ejecutar consultas en la base de datos
        mcursor = bd.cursor()

        # Consultar la clave en la tabla LLAVE
        sql = "SELECT LLAVE_STR FROM LLAVE"
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

    
    def Iniciar_sesion(e):
        # Obtener la clave de la base de datos
        clave_str = obtener_clave()

        if clave_str is None:
            print("\nNo se pudo obtener la clave de la base de datos")
            return
        # Crear un objeto Fernet con la clave obtenida de la base de datos
        objeto_cifrado = Fernet(clave_str.encode('utf-8'))

        # Desencriptar la clave utilizando el objeto de cifrado
        print(f"\nkey cifrada en bits encode:{objeto_cifrado}")
        print(f"\nClave srt:{clave_str}")

        # Conectar a la base de datos MySQL
        bd = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="Billify"
        )

        # Crear un cursor para ejecutar consultas en la base de datos
        mcursor = bd.cursor()
        # Obtener el valor del campo de entrada 'Usuario'
        usuario = Usuario.value
        contraseña=Password.value

        # Crear una consulta SQL para obtener la contraseña del usuario de la base de datos
        sql = "SELECT CLAVES FROM REGISTRO WHERE USUARIOS = '{}'".format(usuario)
        # Ejecutar la consulta SQL
        mcursor.execute(sql)
        # Obtener el resultado de la consulta
        resultado = mcursor.fetchone()
        bd.close()
        # Si se encontró un resultado, imprimir la clave

        if resultado:
            # Obtener la clave cifrada desde la base de datos
            clave_cifrada = resultado[0]
            print(f"\nesta es mi clave cifrada: {clave_cifrada}")
            # Desencriptar la clave utilizando el objeto de cifrado
            texto_desencriptado_bytes = objeto_cifrado.decrypt(clave_cifrada.encode('utf-8'))
            print(f"esta es mi objeto cifrado(key): {objeto_cifrado}")
            print(f"esta es mi texto desincriptado en bytes: {texto_desencriptado_bytes}")
            print(f"esta es la contraseña que ingreso en el gui: {contraseña}")
            # Convertir los bytes desencriptados a cadena de texto
            texto_desencriptado = texto_desencriptado_bytes.decode('utf-8')
            print("La clave del usuario {} es: {}".format(usuario, texto_desencriptado))

            # Validar la contraseña ingresada por el usuario
            if contraseña == texto_desencriptado:
                print("Se permitió entrar.")
                page.go("/page1/:my_id")
            else:
                print("La contraseña es incorrecta. No se permitió el acceso.")
        else:
            print("No se encontró el usuario en la base de datos.")
        

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


    #!Variables de campos de entrada
    Usuario=ft.TextField(label="Usuario", border="underline", hint_text="Ingresa tu usuario",width=250,height=60)
    Password=ft.TextField(label="Contraseña", border="underline", 
        hint_text="Ingresa tu contraseña",width=250,height=60,
        password=True, can_reveal_password=True
        )
    
    Login=ft.Container(
        #width=1700,
        #height=700,
        #border=ft.border.all(),
        padding=0,
        content=
            ft.Column(
                spacing=10,controls=[
                ft.Divider(color=ft.colors.TRANSPARENT),    
                ft.Container(
                    width=1366,
                    padding=0, 
                    #border=ft.border.all(),
                    content=ft.Row(spacing=0,controls=[
                        ft.Card(
                            width=650,
                            height=500,
                            elevation=10,
                            #border=ft.border.all(),
                            content=ft.Row(
                                spacing=0,controls=[
                                ft.Card(
                                    #padding=0,
                                    width=325,
                                    height=600,
                                    #border=ft.border.all(),
                                    content=ft.Image(
                                        #opacity=0.5,
                                        src=f"src/Empresa_fondo.jpg",
                                        fit=ft.ImageFit.FILL,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    )
                                ),
                                ft.Container(
                                    padding=0,
                                    height=500,
                                    width=325,
                                    #border=ft.border.all(),
                                    content=ft.Row([
                                            #ft.Divider(height=10),
                                            ft.Column([
                                                ft.Container(
                                                    width=325,
                                                    content=(ft.Row(spacing=0,controls=[
                                                        ft.Container(width=100,height=100,
                                                            #border=ft.border.all(),
                                                            content=ft.Image(
                                                                src=f"src/Logo.png",
                                                                fit=ft.ImageFit.FILL,
                                                                repeat=ft.ImageRepeat.NO_REPEAT, 
                                                            )            
                                                        )
                                                    ],alignment=ft.MainAxisAlignment.CENTER))
                                                ),
                                                
                                                ft.Container(
                                                    padding=0,
                                                    #height=30,
                                                    width=320,
                                                    #border=ft.border.all(),
                                                    content=ft.Row(spacing=0,controls=[ft.Text("Billify",size=35,weight=ft.FontWeight.W_900,color='#3d5ff5')],
                                                        alignment=ft.MainAxisAlignment.CENTER)
                                                ), 
                                                ft.Container(
                                                    padding=0,
                                                    #height=30,
                                                    width=320,
                                                    #border=ft.border.all(),
                                                    content=ft.Row(spacing=0,controls=[ft.Text("Inicia sesión para acceder a tu cuenta.",
                                                        size=15)],
                                                        alignment=ft.MainAxisAlignment.CENTER)
                                                ), 
                                                ft.Container(
                                                    width=320,
                                                    content=ft.Divider()),
                                                ft.Container(
                                                    padding=10,
                                                    #height=200,
                                                    width=320,
                                                    alignment = ft.alignment.center,
                                                    #alignment=ft.MainAxisAlignment.CENTER,
                                                    #border=ft.border.all(),
                                                    content=ft.Row([
                                                        ft.Column([
                                                            Usuario,Password,
                                                            
                                                        ])
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                ), 
                                                ft.Container(
                                                    width=325,
                                                    alignment=ft.alignment.center,
                                                    content=(
                                                        ft.Row(spacing=0,controls=[
                                                            #ft.VerticalDivider(width=25),
                                                            ft.Column([
                                                                ft.Text(
                                                                    disabled=False,
                                                                    spans=[
                                                                        ft.TextSpan(
                                                                            "¿Olvido su contraseña?",
                                                                            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                                            on_click=lambda _: page.go("/pagina_inventario/:inv"),
                                                                            #url="https://google.com",
                                                                            on_enter=highlight_link,
                                                                            on_exit=unhighlight_link,
                                                                        )
                                                                    ],size=13
                                                                ),
                                                            ])
                                                            
                                                        ],alignment=ft.MainAxisAlignment.CENTER)
                                                    )
                                                ), 
                                                #ft.Divider(),
                                                ft.Container(
                                                    width=325,
                                                    #border=ft.border.all(),
                                                    content=ft.Row([
                                                        ft.ElevatedButton(
                                                            #"Iniciar",
                                                            on_click=Iniciar_sesion,
                                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5,)),
                                                            width=200,
                                                            height=30,
                                                            bgcolor=ft.colors.GREEN_500,
                                                            color=ft.colors.WHITE,
                                                            content=ft.Text("Iniciar",size=26)
                                                        )
                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                ),
                                                #ft.Divider(height=10),
                                                ft.Container(width=325,
                                                    content=(ft.Row(spacing=0,controls=[
                                                        ft.Text(
                                                            disabled=False,
                                                            spans=[
                                                                ft.TextSpan("¿No tienes una cuenta?"),
                                                                ft.TextSpan(
                                                                    "Registrate",
                                                                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE,color=ft.colors.BLUE),
                                                                    on_click=lambda _: page.go("/registrarse/:idk"),
                                                                    on_enter=highlight_link_registrarse,
                                                                    on_exit=unhighlight_link_registrarse,

                                                                    
                                                                ),
                                                            ],size=13
                                                        )

                                                    ],alignment=ft.MainAxisAlignment.CENTER)
                                                    )    
                                                )
                                            ])
                                        ])
                                    )
                                ]),
                        ),
                    ],alignment=ft.MainAxisAlignment.CENTER)
                )
            ])
    )
    
    return ft.View(
        "/",
        controls=[
            Login
        ]
    )
