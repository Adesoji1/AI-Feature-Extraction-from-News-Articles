#Finally, we'll create a main function to process the articles and store the extracted data.
def process_article(article):
    article_text = article['full_text']
    article_metadata = {
        'url': article['url'],
        'date': article['date'],
        'symbol': article['symbol']
    }

    ai_features = extract_ai_features(article_text)
    parsed_data = parse_response(ai_features)
    insert_data_to_db(parsed_data, article_metadata)

# Example usage
articles = [
    {
        "url": "http://example.com/article1",
        "date": "2024-06-01",
        "symbol": "AAPL",
        "full_text": "Full text of the news article..."
    },
    # Add more articles as needed
]

for article in articles:
    process_article(article)
