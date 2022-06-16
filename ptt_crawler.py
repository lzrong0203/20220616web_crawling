import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.ptt.cc{}"


def get_soup(url):
    cookies = {}
    if url == "Gossiping":
        cookies = {"over18": "1"}
    if not url.startswith("/bbs/"):
        link = baseUrl.format("/bbs/" + url)
        # print(link)
    else:
        link = baseUrl.format(url)
        # print(link)

    r = requests.get(link, cookies=cookies)
    return BeautifulSoup(r.text, "html.parser")


def get_title_url(url):
    soup = get_soup(url)
    articles = []
    for title in soup.find_all("div", {"class": "title"}):
        # print("====")
        article = {}
        if title.a is not None:
            article["href"] = title.a["href"]
            article["title"] = title.a.text
            articles.append(article)
    return articles


# def get_stock():
#     try:
#         r = requests.get("https://www.p.cc/bbs/Stoc/")
#         if r.status_code != 200:
#             raise Exception("ERROR!!!")
#     except requests.exceptions.RequestException as e:
#         print(e)
#         return
#     except Exception as e:
#         print(e)
#         return
#     return BeautifulSoup(r.text, "html.parser")

def get_upper_page(url):
    soup = get_soup(url)
    return soup.find_all("a", {"class", "btn wide"})[1].get("href")


if __name__ == "__main__":
    print(get_title_url(get_upper_page("Stock")))
