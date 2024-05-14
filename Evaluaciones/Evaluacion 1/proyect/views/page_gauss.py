import flet as ft
from flet_route import Params, Basket

def page_gauss(page: ft.Page,params: Params,basket: Basket):

    dd_size= ft.Dropdown(
        width=100,
        value="n",
        options=[
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
        ],
    )

    txt_matriz=ft.TextField(value="",read_only=True,multiline=True,min_lines=5)


    return ft.View(
        "/page_gauss/:Reduccion",

        [
            ft.AppBar(title=ft.Text("Conversión de sistemas númericos"), bgcolor=ft.colors.SURFACE_VARIANT),
            
            ft.Row([
                ft.Column([
                    ft.Row([ft.Text("working progress"),dd_size]),

                    ]),
                ft.Column([

                ])
                ]),

            
            ft.ElevatedButton("Go back",on_click=lambda _: page.go("/"))
        ]
    )