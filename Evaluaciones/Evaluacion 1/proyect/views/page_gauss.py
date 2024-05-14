import flet as ft
from flet_route import Params, Basket

def page_gauss(page: ft.Page,params: Params,basket: Basket):

    page.window_height=600
    page.window_width=700

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

    txt_error=ft.Text("error",visible=False,color=ft.colors.RED)
    icon_error=ft.Icon(name=ft.icons.ERROR,visible=False,color=ft.colors.RED)

    txt_matriz=ft.TextField(value="",label="Matriz",read_only=True,multiline=True,min_lines=5,width=250,bgcolor="#5b5b60")
    btn_create=ft.ElevatedButton(text="Crear Matriz",icon=ft.icons.CREATE)
    btn_clean=ft.ElevatedButton(text="Borrar",icon=ft.icons.CLEAR)

    txt_vector=ft.TextField(value="",label="Vector",read_only=True,multiline=True,width=250,bgcolor="#5b5b60")
    txt_vector0=ft.TextField(value="",label="Vector Xo",read_only=True,multiline=True,width=250,bgcolor="#5b5b60")
    txt_resuly=ft.TextField(value="",label="Resultado",read_only=True,multiline=True,min_lines=5,width=250,bgcolor="#5b5b60")

    return ft.View(
        "/page_gauss/:Reduccion",

        [
            ft.AppBar(title=ft.Text("Conversión de sistemas númericos"), bgcolor=ft.colors.SURFACE_VARIANT),
            
            ft.Row([
                ft.Column([
                    ft.Row([ft.Text("Indice de la matriz"),dd_size]),
                        txt_matriz,
                        ft.Row([btn_create,btn_clean]),
                    ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Column([
                    ft.Text("Datos del vector",size=20),
                    txt_vector,
                    ft.Text("Datos del Vector Xo",size=20),
                    txt_vector0,
                    ft.Text("Resultado",size=20),
                    txt_resuly
                ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ]),

            ft.Row([ft.ElevatedButton("Go back",on_click=lambda _: page.go("/")),
                    icon_error,txt_error,
                    ]),
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )