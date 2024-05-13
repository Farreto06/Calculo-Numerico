import flet as ft
from flet_route import Params, Basket

def Home(page: ft.Page,params: Params,basket: Basket):

    return ft.View(
        "/",

        controls=[

            ft.AppBar(title=ft.Text("Seleciona la operacion a Realizar")),
            ft.ElevatedButton("Sistemas Númericos",on_click=lambda _: page.go("/page_sis/Si estoy aqui")),
            ft.ElevatedButton("Reduccion Gausiana",on_click=lambda _: page.go("/page_gauss/Yes, i'm here"))    
            
        ]
    )