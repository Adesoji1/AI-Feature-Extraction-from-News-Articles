
# AI Feature Extraction from News Articles

## Project Overview

This project focuses on extracting specific AI-related features from news articles and storing the parsed information in a PostgreSQL database. The articles are related to specific companies, identified by their company name and stock symbol. The extracted features include AI R&D spending, AI patents, AI research publications, AI product announcements, AI infrastructure investment, and AI talent.

## Features

- Extract AI-related information from news articles using OpenAI's ChatCompletion API.
- Store extracted data in PostgreSQL database tables.
- Handle different types of data (quarterly, annual, event-specific).
- Summarize articles using a language model.

## Database Schema

The project utilizes a PostgreSQL database with the following tables:
- `news_articles`: Stores the news articles and their metadata.
- `ai_rd_spending`: Stores AI R&D spending data.
- `ai_patents`: Stores AI patent data.
- `ai_research_publications`: Stores AI research publication data.
- `ai_product_announcements`: Stores AI product announcement data.
- `ai_infrastructure_investment`: Stores AI infrastructure investment data.
- `ai_talent`: Stores AI talent data.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- OpenAI API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-feature-extraction.git
   cd ai-feature-extraction
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory and add your OpenAI API key and PostgreSQL database URL:
   ```ini
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=postgresql://username:password@localhost/dbname
   ```

5. Set up the PostgreSQL database schema by executing the SQL commands in the `schema.sql` file:
   ```bash
   psql -U username -d dbname -f schema.sql
   ```

### Usage

1. Add your news articles to the `articles.json` file in the following format:
   ```json
   [
       {
           "url": "http://example.com/article1",
           "date": "2024-06-01",
           "symbol": "AAPL",
           "full_text": "Full text of the news article..."
       }
       // Add more articles as needed
   ]
   ```

2. Run the script to process the articles and store the extracted data in the database:
   ```bash
   python main.py
   ```

## Code Explanation

### main.py

This script processes the news articles, extracts AI-related features using the OpenAI API, and stores the parsed data in the PostgreSQL database.

### database.py

This module contains functions for connecting to the PostgreSQL database using `psycopg2` and `SQLAlchemy`.

### extraction.py

This module contains functions for interacting with the OpenAI API and parsing the responses to extract relevant AI-related data.

### utils.py

This module contains utility functions for handling errors and inserting data into the database tables.

## Future Enhancements

- Improve the parsing logic to accurately extract AI feature data from the ChatCompletion API responses.
- Enhance error handling and edge case management.
- Implement more detailed logging and monitoring.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
```

### `.env` File Example
Create a `.env` file in the project root directory with the following content:

```ini
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://username:password@localhost/dbname
```

### `requirements.txt`
Ensure your `requirements.txt` includes the necessary dependencies:

```plaintext
psycopg2-binary
sqlalchemy
openai
python-dotenv
```

### `schema.sql`
Create a `schema.sql` file for your database schema:

```sql
CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    date DATE NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    full_text TEXT NOT NULL,
    llm_full_text_summary TEXT
);

CREATE TABLE ai_rd_spending (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    data_type VARCHAR(20) NOT NULL,
    year INT,
    quarter INT,
    event_date DATE,
    category TEXT,
    value NUMERIC,
    url TEXT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE ai_patents (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    data_type VARCHAR(20) NOT NULL,
    year INT,
    quarter INT,
    event_date DATE,
    category TEXT,
    value TEXT,
    url TEXT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE ai_research_publications (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    data_type VARCHAR(20) NOT NULL,
    year INT,
    quarter INT,
    event_date DATE,
    category TEXT,
    value TEXT,
    url TEXT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE ai_product_announcements (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    data_type VARCHAR(20) NOT NULL,
    year INT,
    quarter INT,
    event_date DATE,
    category TEXT,
    value TEXT,
    url TEXT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE ai_infrastructure_investment (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    data_type VARCHAR(20) NOT NULL,
    year INT,
    quarter INT,
    event_date DATE,
    category TEXT,
    value NUMERIC,
    url TEXT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE ai_talent (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    data_type VARCHAR(20) NOT NULL,
    year INT,
    quarter INT,
    event_date DATE,
    category TEXT,
    value TEXT,
    url TEXT NOT NULL,
    date DATE NOT NULL
);
```

