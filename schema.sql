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
