# stock-news-headlines
Sentiment Analysis, Word2Vec Embedding, and LSTM Modeling of News Headlines to Classify Stock Market Movements

## Data Collection
Two different types of data were collected for this project: news article headlines and historical stock market prices for the SPY ticker symbol.
News headlines were scraped from the news archives of The Wall Street Journal and The New York Times. In order to scrape headlines, I used selenium and the code for that process can be found in **`headline-data-collection.py`**.
The historical stock prices for SPY were obtained from the Alpha Vantage API TIME_SERIES_DAILY endpoint. That code can be found in **`stock-data-collection.py`**.

## Data Cleaning
