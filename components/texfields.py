import flet as ft

def main(page):
    page.title = "TextField Styles Demo"

    # TextField básico
    basic_textfield = ft.TextField(label="Basic TextField", hint_text="Enter text here")

    # TextField con fondo relleno
    filled_textfield = ft.TextField(label="Filled TextField", hint_text="Enter text here", filled=True)

    # TextField con borde resaltado cuando está enfocado
    focused_border_textfield = ft.TextField(
        label="Focused Border TextField",
        hint_text="Enter text here",
        focused_border_color=ft.colors.BLUE,
        focused_border_width=2
    )

    # TextField con diferentes colores de texto
    colored_textfield = ft.TextField(
        label="Colored TextField",
        hint_text="Enter text here",
        color=ft.colors.GREEN,
        focused_color=ft.colors.RED
    )

    # TextField con diferentes estilos de texto
    styled_textfield = ft.TextField(
        label="Styled TextField",
        hint_text="Enter text here",
        text_style=ft.TextStyle(size=20, weight="bold", color=ft.colors.PURPLE)
    )

    # TextField con icono
    icon_textfield = ft.TextField(
        label="Icon TextField",
        hint_text="Enter text here",
        icon=ft.icons.SEARCH
    )

    # TextField con borde personalizado
    custom_border_textfield = ft.TextField(
        label="Custom Border TextField",
        hint_text="Enter text here",
        border=ft.InputBorder.OUTLINE,
        border_color=ft.colors.ORANGE,
        border_width=2,
        border_radius=10
    )

    # TextField con fondo de diferentes colores en diferentes estados
    state_color_textfield = ft.TextField(
        label="State Color TextField",
        hint_text="Enter text here",
        fill_color=ft.colors.LIGHT_BLUE,
        focused_bgcolor=ft.colors.LIGHT_GREEN,
        bgcolor=ft.colors.LIGHT_BLUE
    )

    # TextField con padding personalizado
    padded_textfield = ft.TextField(
        label="Padded TextField",
        hint_text="Enter text here",
        content_padding=20
    )

    # TextField con un contador de caracteres
    counter_textfield = ft.TextField(
        label="Counter TextField",
        hint_text="Enter text here",
        counter_text="0/100",
        counter_style=ft.TextStyle(size=12, color=ft.colors.RED)
    )

    # TextField con texto de ayuda
    helper_textfield = ft.TextField(
        #label="Helper TextField",
        hint_text="Enter text here",
        helper_text="This is a helper text",
        helper_style=ft.TextStyle(size=12, color=ft.colors.LIGHT_GREEN_ACCENT_700)
    )

    # TextField con texto de error
    error_textfield = ft.TextField(
        #label="Error TextField",
        hint_text="Enter text here",
        error_text="This is an error text",
        error_style=ft.TextStyle(size=12, color=ft.colors.RED)
    )

    # Agregar todos los TextFields a la página
    page.add(
        basic_textfield,
        filled_textfield,
        focused_border_textfield,
        colored_textfield,
        styled_textfield,
        icon_textfield,
        custom_border_textfield,
        state_color_textfield,
        padded_textfield,
        counter_textfield,
        helper_textfield,
        error_textfield
    )

ft.app(target=main)
