import flet as ft
from flet_route import Params,Basket


def inventario(page: ft.Page,params: Params, basket: Basket):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window_maximized=True
    page.window_title_bar_hidden = True
    page.padding=0
    rail = ft.NavigationRail(
        
        width=130,
        height=700,
        #bgcolor=ft.colors.AMBER,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        #extended=True,
        #bgcolor= ft.colors.GREEN_200,
        indicator_shape=ft.StadiumBorder(),
        elevation=20,
        #scale=1.03,
    
        #leading=(ft.Image("banner.png",width=100)),
        group_alignment=-1,
        destinations=[
    
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED, 
                selected_icon=ft.icons.HOME, 
                label="Menu principal",padding=13 
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SHOPPING_CART_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.SHOPPING_CART_ROUNDED),
                label="Facturas",padding=15
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.ADD_ROUNDED),
                label_content=ft.Text("Generar facturas"),padding=13
            ),
            ft.NavigationRailDestination(
                selected_icon=ft.icons.GROUP_ROUNDED,
                icon=ft.icons.GROUP_OUTLINED,
                label_content=ft.Text("Clientes"),padding=13
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INVENTORY_2_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.INVENTORY_2_ROUNDED),
                label_content=ft.Text("Inventario"),padding=13
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.QUERY_STATS_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.QUERY_STATS_ROUNDED),
                label_content=ft.Text("Estadisticas"),padding=13
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.ADD_ROUNDED),
                label_content=ft.Text("Configuraciones"),padding=13
            ),
        ],
        #on_change=lambda e: change_index(e.control.selected_index),

    )
    page_four_ui=ft.Column([
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
                                    ft.Text("FUNCIONAAAAAAA",weight=ft.FontWeight.W_900,color='#3d5ff5',size=18),
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
                    content=ft.Row([rail])
                ) 
            ],alignment=ft.MainAxisAlignment.START)
            
        )
        ]
    )
    content = ft.Row([page_four_ui],vertical_alignment=ft.MainAxisAlignment.START)
    def change_index(e):
        index = e
        if index == 0:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 0
            page.go("/page1/:my_id")
            #content.controls.append(page_one_ui)
            page.update()

        if index == 1:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 1
            #content.controls.append(page_two_ui)
            page.update()

        if index == 2:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 2
            #content.controls.append(page_three_ui)
            page.go("/page1/:my_id")
            page.update()
        if index == 3:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 3
            #content.controls.append(page_four_ui)
            page.go("/page1/:my_id")
            page.update()
        if index == 4:
            print(str(index))
            content.controls.pop()
            rail.selected_index = 4
            #content.controls.append(page_five_ui)
            page.go("/")
            page.update()
        if index == 5:
            print(str(index))
            rail.selected_index = 4
            page.go("/page1/:my_id")
            page.update()
    return ft.View(
        "/inventario/:inv",
        controls=[
            page_four_ui
        ]
    )