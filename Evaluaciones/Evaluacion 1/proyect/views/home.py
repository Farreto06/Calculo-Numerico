import flet as ft
from flet_route import Params, Basket

def Home(page: ft.Page,params: Params,basket: Basket):

    page.window_height=400
    page.window_width=350

    return ft.View(
        "/",

        [
            ft.AppBar(title=ft.Text("Menu"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text(value="Seleciona la operacion a Realizar",text_align=ft.TextAlign.CENTER,width=350),
            ft.ElevatedButton("Sistemas Númericos",on_click=lambda _: page.go("/page_sis/Si estoy aqui")),
            ft.ElevatedButton("Reduccion Gausiana",on_click=lambda _: page.go("/page_gauss/Yes, i'm here"))    
            
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
        
    )