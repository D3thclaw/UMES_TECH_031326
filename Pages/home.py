from nicegui import ui
from Components.navbar import navbar


@ui.page('/')
def home_page():
    navbar()

    ui.label('Home Page').classes('text-2xl')

    ui.button('Go to Dashboard', on_click=lambda: ui.navigate.to('/dashboard'))
