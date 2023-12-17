from bs4 import BeautifulSoup
import requests
import time
import random

url_content = ["https://top.zhan.com/toefl/speak/alltpo66.html", "https://top.zhan.com/toefl/speak/alltpo62.html",
               "https://top.zhan.com/toefl/speak/alltpo58.html", "https://top.zhan.com/toefl/speak/alltpo54.html",
               "https://top.zhan.com/toefl/speak/alltpo48.html", "https://top.zhan.com/toefl/speak/alltpo44.html",
               "https://top.zhan.com/toefl/speak/alltpo40.html", "https://top.zhan.com/toefl/speak/alltpo36.html",
               "https://top.zhan.com/toefl/speak/alltpo32.html", "https://top.zhan.com/toefl/speak/alltpo28.html",
               "https://top.zhan.com/toefl/speak/alltpo24.html", "https://top.zhan.com/toefl/speak/alltpo20.html",
               "https://top.zhan.com/toefl/speak/alltpo16.html", "https://top.zhan.com/toefl/speak/alltpo12.html",
               "https://top.zhan.com/toefl/speak/alltpo8.html", "https://top.zhan.com/toefl/speak/alltpo4.html"
               ]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}  # Do not change this, or response.text(results) might be different.

database = {

}  # test_number: [link1, link2, link3, link4]

for u in url_content:
    response = requests.get(u, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

    # html = open('ExampleHTML/index_example.html').read()
    # soup = BeautifulSoup(html, "html.parser")

    # div(test number) -> h2
    #                  -> ... -> links*4

    divs = soup.find_all('div', {'class': 'cssExerciseArea'})
    divs = divs[0:int(len(divs) / 2)]
    for i in divs:
        l = []
        for j in i.findChildren('a', {'event_type': 'E_6_14'}):
            l.append(j['href'])
        titles = i.findChildren('h2', {'class': 'cssBodyTit'})[0].get_text(strip=True).removeprefix("Official")
        database[int(titles)] = l

    print(database)
    time.sleep(0.1 * random.randint(50, 100))
