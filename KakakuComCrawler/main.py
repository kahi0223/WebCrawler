from datetime import datetime
from datetime import timedelta
from datetime import timezone
from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup

HEADERS = {"User-Agent":
               "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
PROXYS = {'http':
              'socks5://127.0.0.1:9050'}

URLS = {"売り上げランキング": "https://kakaku.com/kaden/lcd-tv/ranking_2041/",
        "人気ランキング": "https://kakaku.com/kaden/lcd-tv/ranking_2041/hot/"}
OUTPUT_BASE_PATH = "価格コム"


def config() -> None:
    proxies = request.ProxyHandler(proxies=PROXYS)
    request.install_opener(opener=request.build_opener(proxies))


def get_texts(target_url, headers,
              target_tag_name, target_tag_attrs) -> list:
    html = request.urlopen(Request(url=target_url, headers=headers))
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all(name=target_tag_name, attrs=target_tag_attrs)
    texts = [tag.get_text() for tag in tags]
    return texts


def formatting(texts) -> list:
    formatted_list = []

    def format_text(text):
        res = text
        return res

    for text in texts:
        formatted = format_text(text=text)
        formatted_list.append(formatted)

    return formatted_list


def to_contents(brands, titles) -> list:
    contents = []
    for i in range(len(brands)):
        content = ','.join([
            brands[i],
            titles[i],
        ])
        contents.append(content)
    return contents


def output_csv(header, brands, titles, path) -> None:
    with open(file=path, mode="w", encoding='utf_8_sig') as f:
        header = ','.join([
            header
        ])
        print(header, file=f)
        for i in range(len(brands)):
            contents = ','.join([
                str(i + 1),
                brands[i],
                titles[i]
            ])
            print(contents, file=f)


if __name__ == '__main__':
    config()
    today = datetime.now(tz=timezone(timedelta(hours=9))).strftime("%y%m%d")
    for key, url in URLS.items():
        URL = url
        brands = get_texts(target_url=URL,
                           headers=HEADERS,
                           target_tag_name="span",
                           target_tag_attrs={'class': "rkgBoxNameMaker"})
        titles = get_texts(target_url=URL, headers=HEADERS,
                           target_tag_name="span",
                           target_tag_attrs={'class': "rkgBoxNameItem"})
        output_csv(header=key,
                   brands=brands,
                   titles=titles,
                   path=OUTPUT_BASE_PATH + "_" + key + "_" + today + ".csv")
