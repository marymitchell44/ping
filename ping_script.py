import requests
import time
from datetime import datetime

# URL для посещения
URL = "http://webdesign-finder.com/cogniart/404"

# Заголовки
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Прокси (замените на свои данные)
PROXIES = {
    "http": "http://202.61.204.51:80",
    "https": "http://202.61.204.51:80"
}

# Функция для посещения сайта
def visit_site():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(URL, headers=HEADERS, proxies=PROXIES, timeout=30)
        if response.status_code == 200:
            print(f"[{now}] Сайт успешно посещён. Код ответа: {response.status_code}")
        else:
            print(f"[{now}] Ошибка при посещении сайта. Код ответа: {response.status_code}")
    except Exception as e:
        print(f"[{now}] Ошибка: {e}")

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
