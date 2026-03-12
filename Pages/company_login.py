from nicegui import ui
from Components.navbar import navbar, company_navbar
from database import connect_db


@ui.page('/')
def login_page():
    company_navbar()

    # Full screen centered container
    with ui.row().classes('w-full h-screen items-center justify-center bg-gray-50'):

        # Main login card
        with ui.card().classes('w-[750px] p-0 shadow-xl rounded-2xl overflow-hidden'):

            with ui.row().classes('w-full'):

                # LEFT SIDE (Logo area)
                with ui.column().classes('w-1/2 bg-gray-100 items-center justify-center p-10'):
                    
                    # Replace with your logo
                    ui.image('/static/logo.png').classes('w-40')

                    ui.label('Your Company').classes(
                        'text-xl font-semibold mt-6 text-gray-700'
                    )

                    ui.label(
                        'Secure company portal access'
                    ).classes('text-sm text-gray-500 text-center')


                # RIGHT SIDE (Login form)
                with ui.column().classes('w-1/2 p-8 justify-center'):

                    ui.label('Login').classes(
                        'text-2xl font-bold mb-6'
                    )

                    email = ui.input('Email').classes('w-full')
                    password = ui.input(
                        'Password',
                        password=True
                    ).classes('w-full')

                    def login():
                        if not email.value or not password.value:
                            ui.notify(
                                "Please fill in all fields",
                                type="negative"
                            )
                            return

                        conn = connect_db()
                        cursor = conn.cursor()

                        cursor.execute(
                            "SELECT * FROM users WHERE email=? AND password=?",
                            (email.value, password.value)
                        )

                        user = cursor.fetchone()
                        conn.close()

                        if user:
                            ui.notify(
                                "Login successful",
                                type="positive"
                            )
                            ui.navigate.to('/dashboard')
                        else:
                            ui.notify(
                                "Invalid credentials",
                                type="negative"
                            )

                    ui.button(
                        'Login',
                        on_click=login
                    ).classes(
                        'w-full mt-6 bg-blue-600 hover:bg-blue-700 '
                        'text-white font-semibold py-2 rounded-xl'
                    )

                    ui.button(
                        'Register',
                        on_click=lambda: ui.navigate.to('/register')
                    ).classes(
                        'w-full mt-2 bg-gray-200 hover:bg-gray-300 '
                        'text-black font-medium py-2 rounded-xl'
                    )