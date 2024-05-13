import flet as ft
from views.home import Home
from views.page_sis import page_sis
from views.page_sis import page_sis

def main(page: ft.Page):
    page.title="Menu"
    page.window_height=400
    page.window_width=350
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    page.theme_mode=ft.ThemeMode.LIGHT

    text=ft.Text(value="Seleciona la operacion a Realizar",text_align=ft.TextAlign.CENTER,width=350)
    b_Sis_Num=ft.TextButton(text="Sistemas Númericos")
    b_Gauss=ft.TextButton(text="Reduccion Gausiana")

    page.add(ft.Column([text,b_Sis_Num,b_Gauss]))

ft.app(main)
