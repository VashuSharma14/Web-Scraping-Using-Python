from bs4 import BeautifulSoup
import requests
import pandas as pd

# getting search query and embedding it into 'get' request.
query = input("Enter the product name: ").strip().replace(" ","+")

# putting the query at proper place
html_text = requests.get("https://www.flipkart.com/search?q="+query+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text

# storing the obtained html text into soup variable.
soup = BeautifulSoup(html_text, 'lxml')

# scrapping all the neccessary information as lists from the first page of the website requested.
names = soup.find_all('div', class_='_4rR01T')
prices = soup.find_all('div', class_='_30jeq3 _1_WHN1')
ratings = soup.find_all('div', class_='_3LWZlK')
images = soup.find_all('img', class_='_396cs4 _3exPp9')
links = soup.find_all('a', class_='_1fQZEK')

# creating a dictionary.
dict = {'Product Name':[], 'Rating':[], 'Price':[],'Image':[], 'Link':[]}

# adding all the info into dictionary.
for i in range(0,len(names)):
    dict['Product Name'].append(names[i].text)
    dict['Price'].append(prices[i].text)
    dict['Rating'].append(ratings[i].text+" *")
    dict['Image'].append(images[i]["src"])
    dict['Link'].append("https://www.flipkart.com"+links[i]["href"])

# exporting all the content of dictionary into an xlsx file
df = pd.DataFrame(dict)
df.to_excel('./Products.xlsx', sheet_name="Products")
