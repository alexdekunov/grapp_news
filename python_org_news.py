import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text  # ищем строку с а и копируем текст между <>
            url = news.find('a')['href']  # ищем а и копируем ссылку через ['href']
            published = news.find('time').text  # ищем time и копируем дату публикации
            # добавляем в наш список в виде словаря (список словарей)
            result_news.append({
                "title": title,
                "url": url,
                "published": published
            })
        return result_news
    return False

#
# if __name__ == "__main__":
#     html = get_html("https://www.python.org/blogs/")
#     if html:
#         # [1] копируем страницу с кодом с сайта полностью
#         # with open("python.org.html", "w", encoding="utf8") as f:
#         #     f.write(html)
#
#         # [2] печатаем наш список словорей
#         news = get_python_news(html)
#         print(news)
