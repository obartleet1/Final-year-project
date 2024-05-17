import requests as re
from bs4 import BeautifulSoup
import os
# the URL being scraped vv this is to check the status of the website eg. online or offline
URL = "https://www.kaggle.com"
response = re.get(URL)

print("response -->", response, "\ntype -->", type(response))

print("text --> ", response.text, "\ncontent --> ", response.content, "\nstatus_code --> ", response.status_code)

# 500 --> internal server error (status code)
# 503 --> service in server is unavailable
if response.status_code != 200:
    print("HTTP connection is not successful! Try again.")
else:
    print("HTTP connection is successful!")

soup = BeautifulSoup(response.content, "html.parser")
print("title with tags -->", soup.title, "\ntitle without tags -->", soup.title.text)

for link in soup.find_all("link"):
    print(link.get("href"))

    print(soup.get_text())

    # 1 CREATE A FOLDER TO SAVE HTML FILES
    folder = "mini_dataset"

    if not os.path.exists(folder):
        os.mkdir(folder)

    # 2 DEFINE A FUNCTION THAT SCRAPES AND RETURNS IT
def scrape_content(URL):
    response = re.get(URL)
    if response.status_code == 200:
        print("HTTPS connection is successful! for URL:", URL)
        return response
    else:
        print("HTTPS connection is NOT successful! for URL:", URL)
        return None

    # 3 DEFINE A FUNCTION TO SAVE A HTML FILE OF THE SCRAPED WEBPAGE IN A DIRECTORY
path = os.getcwd() + "/" + folder

def save_html(to_where, text, name):
    file_name = name + ".html"
    with open(os.path.join(to_where, file_name), "w") as f:
        f.write(text)

text_text = response.text
save_html(path, text_text, "example")
# text_text should be test_text but there is an error which doesn't create a new file in mini_dataset

    # 4 DEFINE A URL LIST VARIABLE

URL_list = [
    "https://www.kaggle.com",
    "https://github.com/",
    "https://www.wikipedia.org/",
    "https://www.bbc.co.uk/news",
    "https://news.sky.com/uk",
    "https://www.metoffice.gov.uk/",
    "https://edition.cnn.com/",
    "https://www.espn.co.uk/",
    "https://uk.yahoo.com/",
    "https://www.msn.com/",
]
    # 5 DEFINE A FUNCTION WHICH TAKES THE URL LIST and RUN STEP 2 and 3 for EACH URL
def create_mini_dataset(to_where, URL_list):
    for i in range(0, len(URL_list)):
        content = scrape_content(URL_list[i])
        if content is not None:
            save_html(to_where, content.text, str(i))
        else:
            pass
    print("Mini dataset is created!")

create_mini_dataset(path, URL_list)
    # 6 CHECK IF YOU HAVE 10 DIFFERENT HTML FILES

