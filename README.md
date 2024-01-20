# stock-news-headlines
Sentiment Analysis, Word2Vec Embedding, and LSTM Modeling of News Headlines to Classify Stock Market Movements

## Data Collection
Two different types of data were collected for this project: news article headlines and historical stock market prices for the SPY ticker symbol.
News headlines were scraped from the news archives of The Wall Street Journal and The New York Times. In order to scrape headlines, I used selenium and the code for that process can be found in **`headline-data-collection.py`**.
The historical stock prices for SPY were obtained from the Alpha Vantage API TIME_SERIES_DAILY endpoint. That code can be found in **`stock-data-collection.py`**.

## Data Cleaning
This part can be found in the file **`sentiment-analysis.ipynb`** along with the remaining parts mentioned in this **`README.md`**.
Data cleaning simply involved engineering the feature that we will be trying to predict, which is whether the price increased or decreased 12 days into the future. This was done by shifting the timeseries of stock prices up 12 rows and comparing that future price to the current price. This DataFrame with the new column **`price_increased`** was then merged with the news headline DataFrame. Finally, all punctuation was removed from the article headlines.

## Sentiment Intensity Analysis and Logistic Regression Model
The NLTK module's pre-trained Sentiment Intensity Analyzer was used to produce a positive, neutral, and negative sentiment score for each headline. These sentiment scores were then used as features to train and test a Logistic Regression classifier model that predicts whether stock market price increases or decreases in the future.

**Accuracy: 0.5960**
**Classification Report:**

              precision    recall  f1-score   support

       False       0.00      0.00      0.00       467
        True       0.60      1.00      0.75       689

As can be seen, the Logistic Regression model with sentiment features was not very effective. In fact, nearly all of the model's predictions were of the same class, `True`. I then attempted to make a second, more accurate model using a combination of Word2Vec embeddings and LSTM neural network.

## Word2Vec Embeddings with Long Short-Term Memory Neural Network
I concatenated all article headlines of the same date together so that each date only appears once in the DataFrame. I then used the gensim module's Word2Vec model to create vectorized embeddings for each word in my headlines dataset. I then pad the sequences of word embeddings so that they are all of the same length and then use them to train and test the LSTM model. This LSTM model contains 64 LSTM units and 1 dense output layer. The loss function is Binary Cross Entropy.

**Accuracy: 0.5934**

Unfortunately, there was no improvement between the first model and this LSTM model. The reasons for this lack of effectiveness will be discussed in the below section.

## Areas of Improvement
