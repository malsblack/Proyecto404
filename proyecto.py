import flet as ft
from flet import *
import json
from config.utilities import Accessibility_Focused,Modern_Technological,Warm_Friendly,Professional_Sober,Modern_Classic,Elegant_Contemporary,Dynamic_Vibrant,Minimalist_Chic

def main(page: ft.Page):
    # Define the color scheme
    tema=Accessibility_Focused()
    Background=tema['Background']
    Menus=tema['Menus']
    Text_and_UI_elements=tema['Text_and_UI_elements']
    Action_Buttons=tema['Action_Buttons']
    Alerts_and_Warnings=tema['Alerts_and_Warnings']
    Emphasis_Elements=tema['Emphasis_Elements']


    page.bgcolor=None
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
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("Monitoreo de red",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=Action_Buttons,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,),
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("Monitoreo de red",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=Action_Buttons,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,),
                ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.REDUCE_CAPACITY,color=Text_and_UI_elements), ft.Text("Monitoreo de red",color=Text_and_UI_elements,font_family="Garet")], alignment="center", spacing=10),bgcolor=Action_Buttons,shape=ft.RoundedRectangleBorder(radius=40),width=200,mini=True,),

            ]
        ),
        bgcolor=Menus,  # Establece el color de fondo del contenedor del sidebar a gris
        padding=0,

    )
    sidebar_conteiner.alignment=alignment.top_left

    # Main area where the network topology will be displayed
    # For demonstration purposes, we'll represent it with a placeholder.
    topology_placeholder = ft.Text("Network Topology Diagram Placeholder", color=Background)

    # Layout the sidebar and the main area in a row
    content = ft.Row(
        controls=[sidebar_conteiner, topology_placeholder],
        alignment="start"
    )

    # Set the page title and add the content to the page
    page.title = "Network Topology"
    page.update()
    page.add(content)

# Run the app
ft.app(target=main)
