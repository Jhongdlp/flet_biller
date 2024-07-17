import flet as ft

#!Vista previa
def example(page):
    class Task(ft.UserControl):
        def __init__(self, task_name, task_status_change, task_delete):
            super().__init__()
            self.completed = False
            self.task_name = task_name
            self.task_status_change = task_status_change
            self.task_delete = task_delete

        def build(self):
            self.display_task = ft.Checkbox(
                value=False, label=self.task_name, on_change=self.status_changed
            )
            self.edit_name = ft.TextField(expand=1)

            self.display_view = ft.Row(
                alignment="spaceBetween",
                vertical_alignment="center",
                controls=[
                    self.display_task,
                    ft.Row(
                        spacing=0,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.CREATE_OUTLINED,
                                tooltip="Editar",
                                on_click=self.edit_clicked,
                            ),
                            ft.IconButton(
                                ft.icons.DELETE_OUTLINE,
                                tooltip="Borrar",
                                on_click=self.delete_clicked,
                            ),
                        ],
                    ),
                ],
            )

            self.edit_view = ft.Row(
                visible=False,
                alignment="spaceBetween",
                vertical_alignment="center",
                controls=[
                    self.edit_name,
                    ft.IconButton(
                        icon=ft.icons.DONE_OUTLINE_OUTLINED,
                        icon_color=ft.colors.GREEN,
                        tooltip="Update To-Do",
                        on_click=self.save_clicked,
                    ),
                ],
            )
            return ft.Column(controls=[self.display_view, self.edit_view])

        def edit_clicked(self, e):
            self.edit_name.value = self.display_task.label
            self.display_view.visible = False
            self.edit_view.visible = True
            self.update()

        def save_clicked(self, e):
            self.display_task.label = self.edit_name.value
            self.display_view.visible = True
            self.edit_view.visible = False
            self.update()

        def status_changed(self, e):
            self.completed = self.display_task.value
            self.task_status_change(self)

        def delete_clicked(self, e):
            self.task_delete(self)

    class TodoApp(ft.UserControl):
        def build(self):
            self.expand = True
            self.new_task = ft.TextField(
                hint_text="¿Tienes cosas pendientes?",
                on_submit=self.add_clicked,
                expand=True,
            )
            self.tasks = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)

            self.filter = ft.Tabs(
                selected_index=0,
                scrollable=False,
                on_change=self.tabs_changed,
                tabs=[
                    ft.Tab(text="todos"),
                    ft.Tab(text="activos"),
                    ft.Tab(text="completos"),
                ],
            )

            self.items_left = ft.Text("0 cosas pendientes")

            # application's root control (i.e. "view") containing all other controls
            return ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        controls=[
                            self.new_task,
                            ft.FloatingActionButton(
                                icon=ft.icons.ADD, on_click=self.add_clicked
                            ),
                        ],
                    ),
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment="spaceBetween",
                        vertical_alignment="center",
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Eliminar completos",
                                on_click=self.clear_clicked,
                            ),
                        ],
                    ),
                ],
            )

        def add_clicked(self, e):
            if self.new_task.value:
                task = Task(
                    self.new_task.value, self.task_status_change, self.task_delete
                )
                self.tasks.controls.append(task)
                self.new_task.value = ""
                self.new_task.focus()
                self.update()

        def task_status_change(self, task):
            self.update()

        def task_delete(self, task):
            self.tasks.controls.remove(task)
            self.update()

        def tabs_changed(self, e):
            self.update()

        def clear_clicked(self, e):
            for task in self.tasks.controls[:]:
                if task.completed:
                    self.task_delete(task)

        def update(self):
            status = self.filter.tabs[self.filter.selected_index].text
            count = 0
            for task in self.tasks.controls:
                task.visible = (
                    status == "todos"
                    or (status == "activos" and task.completed == False)
                    or (status == "completos" and task.completed)
                )
                if not task.completed:
                    count += 1
            self.items_left.value = f"{count} cosas por hacer"
            super().update()

    app = TodoApp()
    return ft.SafeArea(app, expand=True)

def view_configuracion_all(page: ft.page):
    page.title="Configuración"
    def Tema1(e):
        page.theme = ft.Theme(color_scheme_seed="RED")
        page.update()

    def Tema2(e):
        page.theme = ft.Theme(color_scheme_seed="PINK")
        page.update()

    def Tema3(e):
        page.theme = ft.Theme(color_scheme_seed="PURPLE")
        page.update()

    def Tema4(e):
        page.theme = ft.Theme(color_scheme_seed="BlUE")
        page.update()

    def Tema5(e):
        page.theme = ft.Theme(color_scheme_seed="GREY")
        page.update()

    def Tema6(e):
        page.theme = ft.Theme(color_scheme_seed="GREEN")
        page.update() 
    
    def Tema7(e):
        page.theme = ft.Theme(color_scheme_seed="YELLOW")
        page.update()

    def Tema8(e):
        page.theme = ft.Theme(color_scheme_seed="ORANGE")
        page.update()
    
    def Tema9(e):
        page.theme = ft.Theme(color_scheme_seed="INDIGO")
        page.update()

    def radiogroup_changed(e):
        # Obtener el modo actual de la página
        current_mode = page.theme_mode

        # Seleccionar el radiobutton correspondiente al modo actual
        if current_mode == ft.ThemeMode.DARK:
            e.control.value = "Modo oscuro"
        elif current_mode == ft.ThemeMode.LIGHT:
            e.control.value = "Modo claro"

        # Cambiar el modo de la página si se selecciona un radiobutton diferente
        if e.control.value == "Modo oscuro":
            page.theme_mode = ft.ThemeMode.DARK
        elif e.control.value == "Modo claro":
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    Configuraciones_page=ft.Container(
            width=1342,
            height=750,
            #border=ft.border.all(),
            content=ft.Column(
                [
                    ft.Container(
                        width=1342,
                        height=40,
                        #border=ft.border.all(),
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.TextButton(
                                            "Volver a la pagina principal", icon="ARROW_BACK",
                                            on_click=lambda _: page.go("/home"),   
                                            
                                        ),
                                        ft.VerticalDivider(width=120),
                                        ft.Text("Configuraciones",size=20),
                                    ]
                                ),
                                ft.Divider(height=10),
                            ]
                        ),
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                width=1342,
                                height=650,
                                #border=ft.border.all(),
                                content=ft.Row([
                                    ft.Card(
                                        elevation=10,
                                        content=ft.Container(
                                            width=500,
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        title=ft.Text("Ajustes de Billify",size=40, weight=ft.FontWeight.W_900, selectable=True,color=ft.colors.BLUE_700),
                                                    ),
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.DARK_MODE_ROUNDED),
                                                        title=ft.Text("Cambiar Tema claro/oscuro"),
                                                    ),
                                                    ft.RadioGroup(content=
                                                        ft.Column([
                                                            ft.Row([
                                                                ft.Text("     ",size=10),
                                                                ft.Radio(value="Modo oscuro",label="Modo oscuro"),
                                                            ]),
                                                            ft.Row([
                                                                ft.Text("     ",size=10),
                                                                ft.Radio(value="Modo claro", label="Modo claro"),
                                                            ])
                                                        ]), on_change=radiogroup_changed),
                                                    #spacing=0,
                                                ]
                                            ),
                                            #padding=ft.padding.symmetric(vertical=10),
                                        )
                                    ),
                                    ft.VerticalDivider(width=30),
                                    ft.Column([
                                        ft.Container(
                                            width=770,
                                            height=140,
                                            #border=ft.border.all(),
                                            content=ft.Card(
                                                elevation=10,
                                                content=ft.Container(
                                                    width=765,
                                                    #height=645,
                                                    padding=10,
                                                    #border=ft.border.all(),
                                                    content=ft.Row([
                                                        ft.Column([
                                                            ft.Text("Temas",size=40, weight=ft.FontWeight.W_900, selectable=True,color=ft.colors.BLUE_700),
                                                            #ft.Divider(color=ft.colors.BLUE_900),
                                                            ft.Row([
                                                                ft.Text("Selecione el tema aqui >>",size=20, weight=ft.FontWeight.W_900, selectable=True),
                                                                ft.PopupMenuButton(
                                                                    icon=ft.icons.COLOR_LENS_OUTLINED,
                                                                    tooltip=("Cambiar tema"),
                                                                    items=[
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.RED),
                                                                                    ft.Text("Color rojo"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema1
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.PINK),
                                                                                    ft.Text("Color rosa"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema2
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.PURPLE),
                                                                                    ft.Text("Color morado"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema3
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.BLUE),
                                                                                    ft.Text("Color azul"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema4
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.CYAN_700),
                                                                                    ft.Text("Color aqua"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema5
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.GREEN),
                                                                                    ft.Text("Color verde"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema6
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.YELLOW),
                                                                                    ft.Text("Color amarillo"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema7
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.ORANGE),
                                                                                    ft.Text("Color naranja"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema8
                                                                        ),
                                                                        ft.PopupMenuItem(
                                                                            content=ft.Row(
                                                                                [
                                                                                    ft.Icon(name=ft.icons.COLOR_LENS_ROUNDED, color=ft.colors.INDIGO),
                                                                                    ft.Text("Color indigo"),
                                                                                ]
                                                                            ),
                                                                            on_click=Tema9
                                                                        ),
                                                                    ], 
                                                                ),
                                                            ]),
                                                            ft.Divider(),
                                                        ])
                                                    ])
                                                )
                                            )
                                        ),
                                        ft.Container(
                                            width=770,
                                            height=490,
                                            #elevation=10,
                                            #border=ft.border.all(),
                                            #border_radius=ft.border_radius.all(10),
                                            content=ft.Row([
                                                ft.Column([
                                                    ft.Text("Vista previa:",size=25, weight=ft.FontWeight.W_900, selectable=True),
                                                    ft.Container(
                                                        width=300,
                                                        height=425,
                                                        padding=10,
                                                        border_radius=ft.border_radius.all(10),
                                                        border=ft.border.all(),
                                                        content=example(page)
                                                    )
                                                ]),
                                            ],alignment=ft.MainAxisAlignment.CENTER)
                                        )
                                    ])
                                    
                                ])
                                
                            )
                            
                        ]
                    ),
                    
                ]
            )
        )
    return ft.Row(
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        Configuraciones_page
                    ]
                )
            )
        ]
    )