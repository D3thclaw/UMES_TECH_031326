# User login page v1
from nicegui import ui
from Components.navbar import navbar
from database import connect_db


@ui.page('/')
def login_page():
    navbar()
    ui.add_head_html('''
    <style>
    body {
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    #bg-carousel {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        transition: background-image 1s ease-in-out;
        z-index: -2;
    }

    #bg-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.45);
        z-index: -1;
    }
    </style>

    <div id="bg-carousel"></div>
    <div id="bg-overlay"></div>

    <script>
    const images = [
        "static/background_img2.jpg",
        "static/background_img1.jpg",
        "static/background_img3.jpg",
    ];

    let index = 0;
    const bg = document.getElementById("bg-carousel");

    function changeBackground() {
        bg.style.backgroundImage = `url(${images[index]})`;
        index = (index + 1) % images.length;
    }

    changeBackground();
    setInterval(changeBackground, 4000);
    </script>
    ''')

    # Full screen centered container
    with ui.column().classes('w-full h-screen items-center justify-center'):

        # Card container
        with ui.card().classes('w-96 p-6 shadow-xl rounded-2xl items-center'):

            # Logo added here
            ui.image('static/Logo2_Transparent.png').classes('w-52 mb-4')

            ui.label('Login').classes('text-2xl font-bold mb-4 text-center')

            email = ui.input('Email').classes('w-full')
            password = ui.input('Password', password=True).classes('w-full')

            def login():
                if not email.value or not password.value:
                    ui.notify("Please fill in all fields", type="negative")
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
                    ui.notify("Login successful", type="positive")
                    ui.navigate.to('/dashboard')
                else:
                    ui.notify("Invalid credentials", type="negative")

            # ✅ Login button (you were missing this)
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