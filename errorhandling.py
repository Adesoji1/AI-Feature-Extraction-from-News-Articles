#We need to ensure the program handles various edge cases and errors gracefully.
def safe_execute(cursor, query, params):
    try:
        cursor.execute(query, params)
    except Exception as e:
        print(f"Error executing query: {e}")

def insert_data_to_db(parsed_data, article_metadata):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for table, records in parsed_data.items():
        for record in records:
            safe_execute(
                cursor,
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
