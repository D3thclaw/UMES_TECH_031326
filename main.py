from nicegui import ui

# ui.label('Hello BOTB26 🚀')

# ui.button('Click me', on_click=lambda: ui.notify('Button clicked!'))

# ui.run()


# import pages so they register
from Pages import home, login, dashboard, register

from database import create_table

create_table()

# auto restart when you save (Useful during development)
ui.run(reload=True)
