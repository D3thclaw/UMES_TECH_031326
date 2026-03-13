from nicegui import ui, app

# ui.label('Hello BOTB26 🚀')

# ui.button('Click me', on_click=lambda: ui.notify('Button clicked!'))

# ui.run()


# import pages so they register
from Pages import login, dashboard, register

from database import create_table
app.add_static_files('/static', 'static')

create_table()

# auto restart when you save (Useful during development)
# ui.run(reload=True)
ui.run(reload=True, storage_secret='your-secret-key')
