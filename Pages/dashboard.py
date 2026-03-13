from nicegui import ui, app
from Components.navbar import navbar


@ui.page('/dashboard')
def dashboard_page():
    navbar()

    with ui.column().classes('w-full h-screen items-center justify-center bg-gray-50'):
        ui.image('static/Logo2_Transparent.png').classes('w-52 mb-4')

        ui.label('What would you like to buy today?') \
            .classes('text-2xl font-bold mb-4 text-center')

        purchase_input = ui.textarea(
            placeholder='Describe what you are looking for...',
        ).classes('w-96')

        def submit():
            if not purchase_input.value:
                ui.notify('Please enter an item you would like to purchase',
                          type='negative')
                return

            # Store in session
            app.storage.user['purchase'] = purchase_input.value

            ui.notify('Saved!', type='positive')

        ui.button(
            'Submit',
            on_click=submit
        ).classes(
            'mt-4 bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg'
        )