from nicegui import ui

# import pages so they register
from Company_pages import company_results, company_login, company_register
from database import create_table

create_table()

# auto restart when you save (Useful during development)
ui.run(reload=True)