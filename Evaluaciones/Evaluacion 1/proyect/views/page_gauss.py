import flet as ft
import numpy as np
from flet_route import Params, Basket

def page_gauss(page: ft.Page,params: Params,basket: Basket):

    page.window_height=600
    page.window_width=700
    page.window_center()

    def create_matriz(e):
        n=int(dd_size.value)
        print("n:",n)
        A = np.random.randint(1, 99, size=(n, n))
        txt_matriz.value=np.array2string(A)
        B = np.random.randint(1, 99, size=n)
        txt_vector.value=np.array2string(B)

        X0=np.zeros(n)
        txt_vector0.value=np.array2string(X0)
        tolera = 1e-6
        iteramax = 1000

        # PROCEDIMIENTO

        # Gauss-Seidel
        tamano = np.shape(A)
        n = tamano[0]
        m = tamano[1]
        #  valores iniciales
        X = np.copy(X0)
        diferencia = np.ones(n, dtype=float)
        errado = 2*tolera

        itera = 0
        while not(errado<=tolera or itera>iteramax):
            # por fila
            for i in range(0,n,1):
                # por columna
                suma = 0 
                for j in range(0,m,1):
                    # excepto diagonal de A
                    if (i!=j): 
                        suma = suma-A[i,j]*X[j]
                
                nuevo = (B[i]+suma)/A[i,i]
                diferencia[i] = np.abs(nuevo-X[i])
                X[i] = nuevo
            errado = np.max(diferencia)
            itera = itera + 1

        # Respuesta X en columna
        X = np.transpose([X])

        # revisa si NO converge
        if (itera>iteramax):
            X=0
        # revisa respuesta
        verifica = np.dot(A,X)

        # SALIDA
        print('respuesta X: ')
        print(X)
        try:
            txt_resuly.value=np.array2string(X)
        except:
            txt_resuly.value="El sistema de ecuaciones no tiene solocion en los Reales"
        
        print('verificar A.X=B: ')
        print(verifica)

        page.update()

    def clear(e) ->None:
        txt_matriz.value=""
        txt_resuly.value=""
        txt_vector.value=""
        txt_vector0.value=""
        page.update()

    dd_size= ft.Dropdown(
        width=100,
        value="1",
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
    btn_create=ft.TextButton(text="Crear Matriz",icon=ft.icons.CREATE,on_click=create_matriz)
    btn_clean=ft.ElevatedButton(text="Borrar",icon=ft.icons.CLEAR,on_click=clear)

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