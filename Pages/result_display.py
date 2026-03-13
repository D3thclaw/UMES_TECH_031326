from nicegui import ui, app
import sqlite3
from datetime import datetime


DB_PATH = 'Data/user_search_results_100.sqlite'


def fetch_relevant_results(user_query):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    keywords = user_query.lower().split()

    cursor.execute("SELECT * FROM user_search_results")
    rows = cursor.fetchall()
    conn.close()

    scored_results = []

    for row in rows:
        score = 0
        title = row['title'].lower()
        snippet = row['snippet'].lower()

        for word in keywords:
            if word in title:
                score += 3      # strong weight
            if word in snippet:
                score += 1      # weaker weight

        if score > 0:
            scored_results.append((score, row))

    # Sort by relevance score DESC
    scored_results.sort(key=lambda x: x[0], reverse=True)

    return [r[1] for r in scored_results]


def log_click(result_id, query, source_engine):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO search_clicks (result_id, query, source_engine, click_timestamp)
        VALUES (?, ?, ?, ?)
    """, (result_id, query, source_engine, datetime.now().isoformat()))

    conn.commit()
    conn.close()


@ui.page('/search-results')
def search_results_page():

    user_query = app.storage.user.get('purchase')

    if not user_query:
        ui.label("No search query found.").classes("text-red-500")
        return

    ui.label(f'Search results for: "{user_query}"').classes(
        "text-2xl font-bold mb-6"
    )

    results = fetch_relevant_results(user_query)

    if not results:
        ui.label("No relevant results found.").classes("text-gray-500")
        return

    # Modal
    with ui.dialog() as dialog, ui.card().classes('w-96'):
        modal_title = ui.label().classes("text-xl font-bold")
        modal_rating = ui.label()
        modal_price = ui.label()
        modal_snippet = ui.label().classes("text-gray-600")

        ui.button("Close", on_click=dialog.close).classes("mt-4")


    def open_modal(result):
        modal_title.set_text(result['title'])
        modal_rating.set_text(
            f"⭐ {result['rating']} ({result['review_count']} reviews)"
        )
        modal_price.set_text(f"Price: ${result['price']}")
        modal_snippet.set_text(result['snippet'])

        log_click(
            result['result_id'],
            user_query,
            result['source_engine']
        )

        dialog.open()


    # Render Results
    with ui.column().classes("items-center w-full"):

        for result in results:

            with ui.column().classes("mb-6 w-full max-w-3xl"):

                ui.label(
                    f"{result['source_engine'].upper()} - Rank #{result['rank_position']}"
                ).classes("text-xs text-gray-400")

                ui.link(
                    result['title'],
                    '#'
                ).classes(
                    "text-xl text-blue-600 hover:underline cursor-pointer"
                ).on(
                    'click',
                    lambda e, r=result: open_modal(r)
                )

                ui.label(result['display_url']).classes(
                    "text-sm text-green-700"
                )

                ui.label(result['snippet']).classes(
                    "text-gray-700"
                )

                ui.label(
                    f"⭐ {result['rating']} • ${result['price']}"
                ).classes("text-sm text-gray-600")