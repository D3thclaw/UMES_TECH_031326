from nicegui import ui
from Components.navbar import navbar
from database import connect_db


@ui.page('/register')
def register_page():
    navbar()

    # 🔥 Background carousel
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
    document.addEventListener("DOMContentLoaded", function() {

        const images = [
            "/static/background_img2.jpg",
            "/static/background_img1.jpg",
            "/static/background_img3.jpg",
        ];

        let index = 0;
        const bg = document.getElementById("bg-carousel");

        function changeBackground() {
            bg.style.backgroundImage = `url(${images[index]})`;
            index = (index + 1) % images.length;
        }

        changeBackground();
        setInterval(changeBackground, 4000);
    });
    </script>
    ''')

    # Centered container (removed bg-gray-50)
    with ui.column().classes('w-full h-screen items-center justify-center'):

        with ui.card().classes(
            'w-96 p-6 shadow-2xl rounded-2xl bg-white/80 backdrop-blur-md'
        ):

            with ui.column().classes('items-center w-full'):
                ui.label('Create Account').classes(
                    'text-2xl font-bold mb-2 text-center'
                )
                ui.image('static/Logo2_Transparent.png').classes('w-52 mb-4')

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

                cursor.execute("SELECT * FROM users WHERE email=?", (email.value,))
                user = cursor.fetchone()

                if user:
                    ui.notify("User already exists", type="negative")
                    conn.close()
                    return

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