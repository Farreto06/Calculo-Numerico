import flet as ft
from flet_route import Params, Basket

def page_gauss(page: ft.Page,params: Params,basket: Basket):

    page.window_height=500
    page.window_width=600

    dd_size= ft.Dropdown(
        width=100,
        bgcolor="#5b5b60",
        options=[
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
        ],
    )

    txt_matriz=ft.TextField(value="",read_only=True,multiline=True,min_lines=5,width=250,bgcolor="#5b5b60")
    btn_create=ft.ElevatedButton(text="Crear Matriz",icon=ft.icons.CREATE)

    return ft.View(
        "/page_gauss/:Reduccion",

        [
            ft.AppBar(title=ft.Text("Conversión de sistemas númericos"), bgcolor=ft.colors.SURFACE_VARIANT),
            
            ft.Row([
                ft.Column([
                    ft.Row([ft.Text("Indice de la matriz"),dd_size]),
                        txt_matriz,
                        btn_create,
                    ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Column([

                ])
                ]),

            
            ft.ElevatedButton("Go back",on_click=lambda _: page.go("/"))
        ]
    )