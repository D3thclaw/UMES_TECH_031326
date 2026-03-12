from nicegui import ui
from Components.navbar import navbar


@ui.page('/login')
def login_page():
    navbar()

    # Full screen centered container
    with ui.column().classes('w-full h-screen items-center justify-center bg-gray-50'):

        # Card container
        with ui.card().classes('w-96 p-6 shadow-xl rounded-2xl'):

            ui.label('Login').classes('text-2xl font-bold mb-4 text-center')

            email = ui.input('Email').classes('w-full')
            password = ui.input('Password', password=True).classes('w-full')

            def login():
                ui.notify(f'Welcome {email.value}')
                ui.navigate.to('/dashboard')

            ui.button(
                'Login',
                on_click=login
            ).classes(
                'w-full mt-4 bg-blue-600 hover:bg-blue-700 '
                'text-white font-semibold py-2 rounded-xl'
            )

            # Register button
            ui.button(
                'Register',
                on_click=lambda: ui.navigate.to('/register')
            ).classes(
                'w-full mt-2 bg-gray-200 hover:bg-gray-300 '
                'text-black font-medium py-2 rounded-xl'
            )
