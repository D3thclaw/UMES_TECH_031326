from nicegui import ui
from Components.navbar import navbar


@ui.page('/dashboard')
def dashboard_page():
    navbar()

    ui.label('Dashboard').classes('text-2xl')

    ui.button('Back Home', on_click=lambda: ui.navigate.to('/'))
