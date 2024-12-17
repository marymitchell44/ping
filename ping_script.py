import cloudscraper
import time
from datetime import datetime

# URL для посещения
URL = "https://webdesign-finder.com/cogniart/404"

# Заголовки
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Список прокси
PROXIES_LIST = [
    {"http": "http://hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001",
     "https": "http://hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001"},
    {"http": "http://hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002",
     "https": "http://hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002"},
]

# Создаем Cloudflare scraper
scraper = cloudscraper.create_scraper()

def visit_site():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for proxy in PROXIES_LIST:
        try:
            print(f"[{now}] Пытаюсь подключиться через прокси: {proxy['http']}")
            response = scraper.get(URL, headers=HEADERS, proxies=proxy, timeout=10)
            if response.status_code == 200:
                print(f"[{now}] Сайт успешно посещён через {proxy['http']}. Код ответа: {response.status_code}")
                return
            else:
                print(f"[{now}] Ошибка при посещении сайта через {proxy['http']}. Код ответа: {response.status_code}")
        except Exception as e:
            print(f"[{now}] Прокси {proxy['http']} не сработал. Ошибка: {e}")
    print(f"[{now}] Все прокси из списка недоступны.")

# Планировщик
def scheduler():
    while True:
        now = datetime.now()
        if 2 <= now.hour < 5:
            visit_site()
            time.sleep(3)
        else:
            print(f"[{now}] Время вне диапазона, ожидание...")
            time.sleep(60)

if __name__ == "__main__":
    scheduler()
