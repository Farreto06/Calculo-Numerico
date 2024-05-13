import flet as ft
from flet_route import Params, Basket

def page_gauss(page: ft.Page,params: Params,basket: Basket):

    return ft.View(
        "/page_gauss/:Reduccion",

        controls=[
            ft.AppBar(title=ft.Text("Conversión de sistemas númericos")),
            ft.Text("working progress"),
            ft.ElevatedButton("Go back",on_click=lambda _: page.go("/"))
        ]
    )