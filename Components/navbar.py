from nicegui import ui


def navbar():
    with ui.row().classes('w-full justify-between items-center bg-gray-200 p-3'):
        ui.label('My App').classes('text-xl font-bold')

        with ui.row():
            ui.button('Home', on_click=lambda: ui.navigate.to('/'))
            ui.button('Dashboard', on_click=lambda: ui.navigate.to('/dashboard'))
            ui.button('Login', on_click=lambda: ui.navigate.to('/login'))

def company_navbar():
    with ui.row().classes('w-full justify-between items-center bg-gray-200 p-3'):
        ui.label('Company Portal').classes('text-xl font-bold')

        with ui.row():
            pass
            #ui.button('Home', on_click=lambda: ui.navigate.to('/'))
            #ui.button('Company Dashboard', on_click=lambda: ui.navigate.to('/dashboard'))
            #ui.button('Company Login', on_click=lambda: ui.navigate.to('/company_login'))