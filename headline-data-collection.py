from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

start_date = datetime(2001, 1, 1)
end_date = datetime(2023, 12, 24)
date_format = "%Y/%m/%d"
nyt_format = "%Y-%m-%d"

driver = webdriver.Firefox()

current_date = start_date

with open('article-data/headlines.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Headline'])
    while current_date <= end_date:
        formatted_date = current_date.strftime(date_format)
        url = f"https://www.wsj.com/news/archive/{formatted_date}"
        try:
            driver.get(url)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'WSJTheme--headlineText--He1ANr9C'))
            )
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            headlines = soup.find_all('span', class_='WSJTheme--headlineText--He1ANr9C')
            for headline in headlines:
                writer.writerow([formatted_date, headline.text])
            next_date = current_date + timedelta(days=1)
            nyt_date = current_date.strftime(nyt_format)
            nyt_next = next_date.strftime(nyt_format)
            url = f"https://www.nytimes.com/search?dropmab=false&endDate={nyt_next}&query=&sections=Business%7Cnyt%3A%2F%2Fsection%2F0415b2b0-513a-5e78-80da-21ab770cb753%2CU.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c%2CWorld%7Cnyt%3A%2F%2Fsection%2F70e865b6-cc70-5181-84c9-8368b3a5c34b&sort=best&startDate={nyt_date}"
            driver.get(url)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'css-2fgx4k'))
            )
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            headlines = soup.find_all('h4', class_='css-2fgx4k')
            for headline in headlines:
                writer.writerow([formatted_date, headline.text])
        except Exception as e:
            print("Error on date " + formatted_date)
        current_date += timedelta(days=1)

driver.close()