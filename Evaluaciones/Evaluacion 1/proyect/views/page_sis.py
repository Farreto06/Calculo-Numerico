import flet as ft
from flet_route import Params, Basket

def page_sis(page: ft.Page,params: Params,basket: Basket):

    page.window_height=400
    page.window_width=500

    return ft.View(
        "/page_sis/:Sistema_Numericos",

        [
            ft.AppBar(title=ft.Text("Conversión de sistemas númericos"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("working progress"),
            ft.ElevatedButton("Go back",on_click=lambda _: page.go("/"))
        ],

        vertical_alignment=ft.MainAxisAlignment.CENTER
    )