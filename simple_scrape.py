
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# load the list of extracted urls
with open('extracted_urls.txt', 'r', encoding='utf-8') as file:
    urls = file.read().splitlines()

def scrape(urls, save_after_n=20):
    # load the extracted_text.csv file
    df = pd.read_csv('extracted_text.csv')

    # remove any URLs from the urls list that are already in the dataframe
    urls = [url for url in urls if url not in df['url'].values]

    # print out how many URLs are left
    print("Number of URLs left:", len(urls))

    data=[]

    for url in urls[:save_after_n]:

        # initialize the variables
        title = ""
        author = ""
        text = ""
        preview = ""

        try:
            # load the url
            response = requests.get(url)
            html_content = response.text
            
            # parse the html
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # extract the title
            title = soup.title.string
            
            # get the document as text
            text = soup.get_text()
            text = text.strip()

            # get the preview
            preview = text[:100].strip()+" ... "+text[-100:].strip()

            # extract the author
            author = soup.find('meta', attrs={'name': 'author'})['content']
        except:
            pass
        
        # add the text to the data variable
        data.append({'url': url, 'title': title, 'author': author, 'preview': preview, 'text': text})
        
        # print the progress
        # print()
        # print("-----")
        print("URL:", url)
        # print("Length:", len(text))
        # print("Preview:"+preview)
        # print("-----")
        # print()

    # concat the dataframes and save the file
    df_update = pd.DataFrame(data=data)

    df = pd.concat([df, df_update])
    print(df.tail())
    print()
    print("Length of the dataframe:", len(df))

    df.to_csv('extracted_text.csv', index=False)

    # sleep for 1 second
    time.sleep(1)

stop_after_n = 20
while stop_after_n > 0:
    scrape(urls, save_after_n=20)
    stop_after_n -= 1