from nicegui import ui
from Components.navbar import navbar
from database import connect_db


@ui.page('/register')
def register_page():
    navbar()

    # Centered container
    with ui.column().classes('w-full h-screen items-center justify-center bg-gray-50'):

        with ui.card().classes('w-96 p-6 shadow-xl rounded-2xl'):

            # Centered header section
            with ui.column().classes('items-center w-full'):
                ui.label('Create Account').classes(
                    'text-2xl font-bold mb-2 text-center'
                )
                ui.image('static/Logo2_Transparent.png').classes('w-52 mb-4')

            # Form fields (full width)
            name = ui.input('Full Name').classes('w-full')
            email = ui.input('Email').classes('w-full')
            password = ui.input('Password', password=True).classes('w-full')
            confirm_password = ui.input(
                'Confirm Password', password=True
            ).classes('w-full')

            def register():

                if not name.value or not email.value or not password.value:
                    ui.notify('Please fill in all fields', type='negative')
                    return

                if password.value != confirm_password.value:
                    ui.notify('Passwords do not match', type='negative')
                    return

                conn = connect_db()
                cursor = conn.cursor()

                # Check if user exists
                cursor.execute("SELECT * FROM users WHERE email=?", (email.value,))
                user = cursor.fetchone()

                if user:
                    ui.notify("User already exists", type="negative")
                    conn.close()
                    return

                # Insert new user
                cursor.execute(
                    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                    (name.value, email.value, password.value)
                )

                conn.commit()
                conn.close()

                ui.notify("Account created!", type="positive")
                ui.navigate.to('/dashboard')

            ui.button(
                'Register',
                on_click=register
            ).classes(
                'w-full mt-4 bg-green-600 hover:bg-green-700 '
                'text-white font-semibold py-2 rounded-xl'
            )

            ui.button(
                'Back to Login',
                on_click=lambda: ui.navigate.to('/')
            ).classes(
                'w-full mt-2 bg-gray-200 hover:bg-gray-300 '
                'text-black font-medium py-2 rounded-xl'
            )
