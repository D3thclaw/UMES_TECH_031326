from nicegui import ui

# import pages so they register
from Pages import company_login, company_register, company_results
from database import create_table

create_table()

# auto restart when you save (Useful during development)
ui.run(reload=True)
