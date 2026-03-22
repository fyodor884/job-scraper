# job scraper 🕵️‍♂️
Scrapes real job listings from websites and delivers clean, ready-to-use datasets (CSV/JSON) for analysis or automation.

## 💡 Use Cases
- Job maket analysis
- Building job aggregator apps 
- Lead generation for recruiters


## 🚀 Features
- Scrapes job title, company, location, date, and apply link
- Saves data into CSV & JSON
- Uses BeautifulSoup + Requests

## 🛠 Tech stack 
- Python
- Requests
- BeautifulSoup (bs4)
- lxml

## 📂 Project Structure
````
job_scrape.py
requirements.txt
README.md
````

## ▶ How to Run
````bash
pip install -r requirements.txt
python job_scrape.py
````

## 📊 Output Example
````json
{
"Job title": "python Developer",
"Company": "XYZ Corp",
"Location":"Remote",
"Date": "2026-03-20" ,
"Apply link: "https://example.com/job"
} 
````
## 🌏Target Website
https://realpython.github.io/fake-jobs/

## 👨 Author
Simple Guy
