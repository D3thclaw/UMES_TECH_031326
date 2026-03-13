from nicegui import ui
import random


@ui.page('/results')#('/search-dashboard')
def dashboard():

    # HEADER 
    with ui.row().classes('w-full items-center justify-between p-4 bg-gray-100'):
        ui.label('Overview: Search Visibility').classes('text-xl font-bold')
        ui.label('How to use').classes('text-gray-500')

    # FILTER BAR
    with ui.row().classes('w-full gap-2 p-4'):
        ui.select(
            ['United States', 'Europe', 'Global'],
            value='Global',
            label='Location'
        ).classes('w-48')

        ui.select(
            ['Last 7 days', 'Last 30 days', 'Last 12 months'],
            value='Last 30 days',
            label='Time range'
        ).classes('w-48')


    # METRIC CARDS 
    with ui.row().classes('w-full gap-4 p-4'):

        def metric_card(title, value, subtitle):
            with ui.card().classes('w-64 p-4'):
                ui.label(title).classes('text-gray-500')
                ui.label(value).classes('text-3xl font-bold text-blue-600')
                ui.label(subtitle).classes('text-sm text-gray-400')

        metric_card(
            'Search Visibility',
            '24.1%',
            '#2 among competitors'
        )

        metric_card(
            'Total Searches',
            '3.1M',
            'Searches last month'
        )

        metric_card(
            'Web Mentions',
            '3.4M',
            'Mentions across search'
        )

        metric_card(
            'AI Mentions',
            '443',
            'Mentions in AI results'
        )


    # TABS 
    with ui.tabs().classes('w-full px-4') as tabs:
        tab1 = ui.tab('Search visibility')
        tab2 = ui.tab('Search demand')
        tab3 = ui.tab('Web mentions')


    #  DATA 
    brands = [
        ('Majestic', 85900, 20200, 48000, 4200),
        ('Ahrefs', 36700, 9000, 24200, 893),
        ('Moz', 16800, 3300, 11500, 568),
        ('SE Ranking', 10100, 3000, 6500, 119),
        ('SpyFu', 3000, 922, 1900, 38),
    ]


    # ----- RESULTS TABLE -----
    with ui.card().classes('w-full m-4 p-4'):

        with ui.row().classes('font-bold text-gray-600 w-full'):
            ui.label('Business').classes('w-40')
            ui.label('All Searches').classes('w-40')
            ui.label('Google').classes('w-40')
            ui.label('AI Results').classes('w-40')
            ui.label('Chatbots').classes('w-40')

        for brand, total, google, ai, chat in brands:

            with ui.row().classes('items-center w-full py-2'):

                ui.label(brand).classes('w-40')

                def bar(value):
                    with ui.row().classes('w-40 items-center'):
                        ui.linear_progress(
                            value=min(value / 100000, 1),
                            show_value=False
                        ).classes('w-32')
                        ui.label(f'{value/1000:.1f}K')

                bar(total)
                bar(google)
                bar(ai)
                bar(chat)



ui.run()