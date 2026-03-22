import requests
import csv
from bs4 import BeautifulSoup
import json
import lxml

# Define a function to scrape jop data from the website

def jop_scrape():
    data=[]

    # Target URL for 
    url='https://realpython.github.io/fake-jobs/'

    # Send the HTTP requests and get the page content
    result=requests.get(url)
    src=result.content

    # Parse the HTML content using lxml parser
    soup=BeautifulSoup(src,'lxml')

    # Find all jops card containers on the page 
    jops=soup.find_all('div',class_="column is-half")

    # Loop through each jop container to extract specific details
    for jop in jops:
         jop_title=jop.find('h2',class_='title is-5').text.strip()
         company=jop.find('h3',class_='subtitle is-6 company').text.strip()
         location=jop.find('p',class_='location').text.strip()
         date=jop.find('p',class_='is-small has-text-grey').text.strip()

         # Get all links within the footer to find the 'Apply' link
         links=jop.find_all('a',class_='card-footer-item')

         # Check if at least two links exist, than take the second one (index 1)
         if len(links) >= 2:
            apply_link= links[1]['href']

        # Append the extracted data as a dictionary to the list
         data.append({
    "Jop title":jop_title,
    "Company":company,
    "Location":location,
    "Date":date,
    "Apply link":apply_link
    })
         
        # Return the final list of dictionary
    return data

# Execute the scraping function and store the result
all_jops=jop_scrape()

# Save the collected data to a CSV file with organized columns
with open(r'jop_toscrape\jop.csv','w',newline='',encoding='utf-8-sig') as jops:
        
        # Use DicWriter to map the dictionary keys to CSV header
        wr=csv.DictWriter(
             jops,
             fieldnames=['Jop title','Company','Location','Date','Apply link'],
             delimiter=';')
        wr.writeheader()
        wr.writerows(all_jops)

# Save the collected data to a JSON file for web or mobile
with open(r'jop_toscrape\jop.json','w',encoding='utf-8') as file:

    # Use json.dump to convert the list of the dictionaries into a json string
    # indent=4 makes the file human-readable , ensure_ascii=False supports non-english characters
    json.dump(all_jops,file,indent=4,ensure_ascii=False)

