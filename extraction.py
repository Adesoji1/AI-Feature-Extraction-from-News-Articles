#We need to parse the API response to extract relevant data and insert it into the database tables.

import json

def parse_response(response):
    # This is a sample parsing function. You may need to adjust it based on the actual response structure.
    data = json.loads(response)
    parsed_data = {
        "rd_spending": data.get("AI R&D Spending"),
        "patents": data.get("AI Patents"),
        "publications": data.get("AI Research Publications"),
        "product_announcements": data.get("AI Product Announcements"),
        "infrastructure_investment": data.get("AI Infrastructure Investment"),
        "talent": data.get("AI Talent")
    }
    return parsed_data

def insert_data_to_db(parsed_data, article_metadata):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for table, records in parsed_data.items():
        for record in records:
            cursor.execute(
                f"""
                INSERT INTO {table} (symbol, data_type, year, quarter, event_date, category, value, url, date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    article_metadata['symbol'], record['data_type'], record['year'], record['quarter'],
                    record['event_date'], record['category'], record['value'], article_metadata['url'], article_metadata['date']
                )
            )
    conn.commit()
    cursor.close()
    conn.close()
