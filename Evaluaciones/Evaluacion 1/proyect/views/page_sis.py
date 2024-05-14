import flet as ft
from flet_route import Params, Basket
from functions.validations import *

def page_sis(page: ft.Page,params: Params,basket: Basket):

    page.window_height=400
    page.window_width=500

    page.window_min_height=400
    page.window_min_width=500

    txt_error=ft.Text("error",visible=False,color=ft.colors.RED)
    icon_error=ft.Icon(name=ft.icons.ERROR,visible=False,color=ft.colors.RED)

    def validation_in(e):
        if dd_in.value!=None and dd_out.value!=None:
            if not(val_in_sis(num_in.value,dd_in.value)):
                txt_error.value="Introdujo un caracter fuera del sistema"
                txt_error.visible=True
                icon_error.visible=True
            else:
                txt_error.value=""
                txt_error.visible=False
                icon_error.visible=False
                conversion(dd_in.value,dd_out.value,num_in.value)
                
        else:
            txt_error.value="No selecciono un sistema"
            txt_error.visible=True
            icon_error.visible=True
            
        page.update()

    def conversion(sis_in,sis_out,num_inp):
        if sis_in=="Hexadecimal":
            if sis_out=="Decimal":
                nd=int(str(num_inp),base=16)
                num_inp=nd
                num_out.value=num_inp
                
            elif sis_out=="Octal":
                nd=int(str(num_inp),base=16)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="4":
                nd=int(str(num_inp),base=16)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="3":
                nd=int(str(num_inp),base=16)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="Binario":
                nd=int(str(num_inp),base=16)
                num_inp=bin(nd)[2:]
                num_out.value=num_inp
            
        elif sis_in=="Decimal":
            if sis_out=="Hexadecimal":
                nd=int(str(num_inp))
                num_inp=hex(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="Octal":
                nd=int(str(num_inp))
                num_inp=oct(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="4":
                nd=int(str(num_inp))
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="3":
                nd=int(str(num_inp))
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="Binario":
                nd=int(str(num_inp))
                num_inp=bin(nd)[2:]
                num_out.value=num_inp
                print(num_inp)

        elif sis_in=="Octal":
            if sis_out=="Hexadecimal":
                nd=int(str(num_inp),base=8)
                num_inp=hex(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="Decimal":
                nd=int(str(num_inp),base=8)
                num_inp=nd
                num_out.value=num_inp
                
            elif sis_out=="4":
                nd=int(str(num_inp),base=8)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="3":
                nd=int(str(num_inp),base=8)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="Binario":
                nd=int(str(num_inp),base=8)
                num_inp=bin(nd)[2:]
                num_out.value=num_inp

        elif sis_in=="4":
            if sis_out=="Hexadecimal":
                nd=int(str(num_inp),base=4)
                num_inp=hex(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="Decimal":
                nd=int(str(num_inp),base=4)
                num_inp=nd
                num_out.value=num_inp
                
            elif sis_out=="Octal":
                nd=int(str(num_inp),base=4)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="3":
                nd=int(str(num_inp),base=4)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="Binario":
                nd=int(str(num_inp),base=4)
                num_inp=bin(nd)[2:]
                num_out.value=num_inp

        elif sis_in=="3":
            if sis_out=="Hexadecimal":
                nd=int(str(num_inp),base=3)
                num_inp=hex(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="Decimal":
                nd=int(str(num_inp),base=3)
                num_inp=nd
                num_out.value=num_inp
                
            elif sis_out=="Octal":
                nd=int(str(num_inp),base=3)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="4":
                nd=int(str(num_inp),base=3)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="Binario":
                nd=int(str(num_inp),base=3)
                num_inp=bin(nd)[2:]
                num_out.value=num_inp

        elif sis_in=="Binario":
            if sis_out=="Hexadecimal":
                nd=int(str(num_inp),base=2)
                num_inp=hex(nd)[2:]
                num_out.value=num_inp
                
            elif sis_out=="Decimal":
                nd=int(str(num_inp),base=2)
                num_inp=nd
                num_out.value=num_inp
                
            elif sis_out=="Octal":
                nd=int(str(num_inp),base=2)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="4":
                nd=int(str(num_inp),base=2)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp

            elif sis_out=="3":
                nd=int(str(num_inp),base=2)
                num_inp=oct(nd)[2:]
                num_out.value=num_inp
            page.update()
        

    num_in=ft.TextField(label="Entrada",width=300,filled=True,border=ft.InputBorder.UNDERLINE)
    num_out=ft.TextField(label="Salida",width=300,filled=True,border=ft.InputBorder.UNDERLINE,disabled=True)

    b_submit=ft.ElevatedButton(text="Convertir",icon=ft.icons.MOVE_DOWN,on_click=validation_in)

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
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("Sistema de salida: "),
            ft.Row([
                num_out,
                dd_out
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("Go back",icon=ft.icons.ARROW_BACK,on_click=lambda _: page.go("/")),b_submit],alignment=ft.MainAxisAlignment.CENTER),

            ft.Row([icon_error,txt_error],alignment=ft.MainAxisAlignment.CENTER)
            
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        
    )