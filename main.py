import flet as ft
from flet_route import Routing,path
from views.Login import Login
from views.page1 import Page_1
from views.Registro import registrarse

#from views.page2 import Page2

def main(page: ft.Page):
    #page.padding=0
    page.theme_mode=ft.ThemeMode.LIGHT
    app_routes=[
        path(url="/",clear=True,view=Login),
        path(url="/page1/:my_id",clear=True,view=Page_1),
        path(url="/registrarse/:idk",clear=True,view=registrarse),
        page.update()
    ]
    
    
    Routing(page=page,
            app_routes=app_routes)
    
    
    page.go(page.route)

#!usar porciacaso
#*,view=ft.AppView.WEB_BROWSER

ft.app(target=main,view=ft.AppView.WEB_BROWSER)