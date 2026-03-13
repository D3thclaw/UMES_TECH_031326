from nicegui import ui


def navbar():
    with ui.row().classes(
            'w-full justify-between items-center bg-gray-200 p-3'
    ):
        # Left side (logo + name)
        with ui.row().classes('items-center gap-2'):
            ui.image('/static/Logo2_Transparent.png').classes('w-20 h-20')
            # ui.label('VeriDAI').classes('text-xl font-bold')

        # Right side
        with ui.row():
            #ui.button('Home', on_click=lambda: ui.navigate.to('/'))
            ui.button('Login', on_click=lambda: ui.navigate.to('/'))
