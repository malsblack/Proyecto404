import flet as ft
from flet import *
import json
from config.utilities import Accessibility_Focused
from tools.connection import *
import telnetlib

# Define the color scheme
tema=Accessibility_Focused()
Background=ft.colors.BLACK12
Menus=tema['Menus']
Text_and_UI_elements=tema['Text_and_UI_elements']
Action_Buttons=tema['Action_Buttons']
Alerts_and_Warnings=tema['Alerts_and_Warnings']
Emphasis_Elements=tema['Emphasis_Elements']


def build_main_page(page: ft.Page):
    # Aquí reconstruyes la interfaz de la página principal
    page.controls.clear()
    main(page)

def router_info_page(page: ft.Page, router_id: str):
    def mostrar_ip_route(e):
        # Aquí va la lógica para mostrar "show ip route"
        resultado_text.value = f"Resultado de 'show ip route' para {router_id}"
        page.update()

    def mostrar_dhcp(e):
        # Aquí va la lógica para mostrar información de DHCP
        resultado_text.value = "Resultado de DHCP"
        page.update()

    def mostrar_dns(e):
        # Aquí va la lógica para mostrar información de DNS
        resultado_text.value = "Resultado de DNS"
        page.update()

    # Limpia la página y agrega los nuevos controles
    page.controls.clear()

    # Área para mostrar los resultados
    resultado_text = ft.Text("")

    # Tamaño común para todos los botones
    boton_tamano = 200

    # Botones para las diferentes consultas
    botones_columna = ft.Column(
        controls=[
            ft.Image(src="config\Images\equipo_404.jpg", width=boton_tamano, height=100),  # Ajusta la altura según necesites
            ft.ElevatedButton(text="Show IP Route", on_click=mostrar_ip_route, width=boton_tamano,bgcolor=Action_Buttons),
            ft.ElevatedButton(text="DHCP", on_click=mostrar_dhcp, width=boton_tamano,bgcolor=Action_Buttons),
            ft.ElevatedButton(text="DNS", on_click=mostrar_dns, width=boton_tamano,bgcolor=Action_Buttons),
            ft.ElevatedButton(text="Volver", on_click=lambda e: build_main_page(page), width=boton_tamano,bgcolor=ft.colors.RED_700)
        ],
        spacing=50,  # Espacio entre los controles
        width=boton_tamano  # Ancho de la columna
    )

    # Columna para el área de texto
    texto_columna = ft.Column(
        controls=[resultado_text],
        expand=1  # Expande para ocupar el espacio restante
    )

    # Layout principal con Row
    layout = ft.Row(
        controls=[botones_columna, texto_columna]
    )

    page.add(layout)
    page.update()


def main(page: ft.Page):

    def mostrar_info_router_bottom_sheet_R1(e):
        router_info_page(page, "R1")

    def mostrar_info_router_bottom_sheet_R2(e):
        router_info_page(page, "R2")

    def mostrar_info_router_bottom_sheet_R3(e):
        router_info_page(page, "R3")

    def mostrar_info_router_bottom_sheet_R4(e):
        router_info_page(page, "R4")

    def mostrar_info_router_bottom_sheet_ISP(e):
        router_info_page(page, "ISP")

    def close_app(e):
        page.window_destroy()


    page.bgcolor=Background
    page.appbar=ft.AppBar(
            leading_width=40,
            title=ft.Text("MONITORIZACION DE RED",font_family="Garet",style=ft.TextThemeStyle.DISPLAY_LARGE,size=20),
            center_title=True,
            bgcolor=Menus
        )

    # Create the image and label for the sidebar
    sidebar_image = ft.Image(src='config\Images\equipo_404.jpg', width=200, height=100)  # Set the width and height as needed
    # Create a sidebar for network actions with the gray background
    sidebar_conteiner=ft.Container(
        content= ft.ListView(
            spacing=50,
            width=200,
            height=900,
            first_item_prototype=True,
            controls=[
                sidebar_image,
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("INICIAR SCANEO",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=Action_Buttons,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,),
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("SCANEO DE UN ROUTER",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=Action_Buttons,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,),
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("REPORTE DE RED",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=Action_Buttons,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,),
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("SALIR",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=ft.colors.RED_700,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,on_click=close_app,)

            ]
        ),
        bgcolor=Menus,  # Establece el color de fondo del contenedor del sidebar a gris
        padding=0,

    )


    image_container = ft.Container(
        content=ft.Image(
            src="config/Images/topologia.jpg",
            width=800,
            height=1000
        ),
        padding=padding.only(left=-200,top=-200,right=-200,bottom=-100),  # Padding superior para mover la imagen hacia arriba
        width=1000,
        height=1200,  # Ajustar la altura del contenedor para incluir el padding,
        alignment=ft.alignment.top_center,
        margin=margin.only(left=0,top=0,right=-100,bottom=0),
        bgcolor=Menus
    )


    topology = ft.Container(
    content=ft.Row(  # Usar Row para organizar horizontalmente
        controls=[
            image_container,
            ft.ListView(
                spacing=30,
                width=200,  # Ajustar la anchura según sea necesario
                height=1000,  # Altura para llenar el contenedor
                first_item_prototype=True,
                controls=[
                    ft.ElevatedButton(
                        text="Consultar R1", 
                        icon="desktop_windows",
                        on_click=mostrar_info_router_bottom_sheet_R1
                        # Aunque no puedas cambiar la posición del ícono, se mostrará junto al texto
                    ),
                    ft.ElevatedButton(
                        text="Consultar R2", 
                        icon="desktop_windows",
                        on_click=mostrar_info_router_bottom_sheet_R2
                        # Aunque no puedas cambiar la posición del ícono, se mostrará junto al texto
                    ),
                    ft.ElevatedButton(
                        text="Consultar R3", 
                        icon="desktop_windows",
                        on_click=mostrar_info_router_bottom_sheet_R3
                        # Aunque no puedas cambiar la posición del ícono, se mostrará junto al texto
                    ),
                    ft.ElevatedButton(
                        text="Consultar R4", 
                        icon="desktop_windows",
                        on_click=mostrar_info_router_bottom_sheet_R4
                        # Aunque no puedas cambiar la posición del ícono, se mostrará junto al texto
                    ),
                        ft.ElevatedButton(
                        text="Consultar ISP", 
                        icon="desktop_windows",
                        on_click=mostrar_info_router_bottom_sheet_ISP
                        # Aunque no puedas cambiar la posición del ícono, se mostrará junto al texto
                    ),




                ]
            )
        ],
        alignment=ft.alignment.top_center
    ),
    bgcolor=Menus,
    expand=True,
    height=1000
)

    # Layout the sidebar and the main area in a row
    content = ft.Row(
        controls=[sidebar_conteiner, topology],
        alignment="start"
    )

    # Set the page title and add the content to the page
    page.title = "Network Topology"
    page.update()
    page.add(content)

# Run the app
ft.app(target=main)
