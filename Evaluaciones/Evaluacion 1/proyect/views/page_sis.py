import flet as ft
from flet_route import Params, Basket
from functions.validations import *

def page_sis(page: ft.Page,params: Params,basket: Basket):

    page.window_height=400
    page.window_width=500

    def validation_in(e):
        val_in_sis(num_in.value,dd_in.value)
        pass
    

    num_in=ft.TextField(label="Entrada",width=300,filled=True,border=ft.InputBorder.UNDERLINE,on_change=validation_in)
    num_out=ft.TextField(label="Salida",width=300,filled=True,border=ft.InputBorder.UNDERLINE,disabled=True)

    b_submit=ft.ElevatedButton(text="Convertir",icon=ft.icons.MOVE_DOWN)

    dd_in = ft.Dropdown(
        width=150,
        options=[
            ft.dropdown.Option("Hexadecimal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("Binario"),
        ],
    )

    dd_out = ft.Dropdown(
        width=150,
        options=[
            ft.dropdown.Option("Hexadecimal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("Binario"),
        ],
    )


    return ft.View(
        "/page_sis/:Sistema_Numericos",

        [
            ft.AppBar(title=ft.Text("Conversión de sistemas númericos"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("Sistema de partida: "),
            ft.Row([
                num_in,
                dd_in
            ]),
            ft.Text("Sistema de salida: "),
            ft.Row([
                num_out,
                dd_out
            ]),
            ft.Row([b_submit,ft.ElevatedButton("Go back",on_click=lambda _: page.go("/"))])
            
        ],

        #vertical_alignment=ft.MainAxisAlignment.CENTER,
        
    )