import flet as ft
from flet_route import Routing, path
from views.home import Home
from views.page_sis import page_sis
from views.page_gauss import page_gauss

def main(page: ft.Page):
    
    app_routes=[
        path(url="/",view=Home),
        path(url="/page_sis/:Sistema_Numericos",view=page_sis),
        path(url="/page_gauss/:Reduccion",view=page_gauss)
    ]

    Routing(page=page,
            app_routes=app_routes)

    page.go(page.route)

ft.app(main)
