import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(response.text, "html.parser")

h2_tags = soup.find_all("h2", class_="title is-5")
p_tags = soup.find_all("p", class_="location")

with open("job_location_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Location"])
    for h2, p in zip(h2_tags, p_tags):
        job_title = h2.text
        location = p.get_text(strip=True)
        writer.writerow([job_title, location])