from dotenv import load_dotenv
import os
import requests
import time
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Загрузка переменных из файла .env
load_dotenv()

# Список URL для посещения
URLS = [
    "http://webdesign-finder.com/towy-v2/404",
    "http://webdesign-finder.com/cogniart/404",
    "http://webdesign-finder.com/deepdigital-v2/404",
]

# Заголовки для имитации браузера
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://google.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

# Список прокси из переменных окружения
PROXIES = [
    {"http": os.getenv("PROXY_0"), "https": os.getenv("PROXY_0")},
    {"http": os.getenv("PROXY_1"), "https": os.getenv("PROXY_1")},
    {"http": os.getenv("PROXY_2"), "https": os.getenv("PROXY_2")},
    {"http": os.getenv("PROXY_3"), "https": os.getenv("PROXY_3")},
    {"http": os.getenv("PROXY_4"), "https": os.getenv("PROXY_4")},
    {"http": os.getenv("PROXY_5"), "https": os.getenv("PROXY_5")},
    {"http": os.getenv("PROXY_6"), "https": os.getenv("PROXY_6")},
    {"http": os.getenv("PROXY_7"), "https": os.getenv("PROXY_7")},
    {"http": os.getenv("PROXY_8"), "https": os.getenv("PROXY_8")},
    {"http": os.getenv("PROXY_9"), "https": os.getenv("PROXY_9")},
]

# Итератор по прокси
proxy_pool = cycle(PROXIES)

# Функция для посещения страницы
def visit_site(url, proxy):
    try:
        print(f"Посещение сайта {url} через прокси: {proxy['http']}")
        response = requests.get(url, headers=HEADERS, proxies=proxy, timeout=1)
        if response.status_code == 200:
            print(f"done: {url}")
        else:
            print(f"error: {url} Код ответа {response.status_code}")
    except Exception as e:
        print(f"error: {url} {e}")

# Основной цикл с проверкой времени
if __name__ == "__main__":
    while True:
        # Получаем текущее серверное время (UTC)
        current_hour = datetime.utcnow().hour

        # Проверяем, что время входит в интервалы работы
        if (0 <= current_hour < 4) or (11 == current_hour and 0 <= current_minute < 45) or (13 == current_hour and 0 <= current_minute < 10):  # 11:00–11:10 и 15:00–15:10 по Киеву
            proxy = next(proxy_pool)  # Получаем следующий прокси из списка
            with ThreadPoolExecutor(max_workers=3) as executor:  # Используем 3 потока
                for url in URLS:
                    executor.submit(visit_site, url, proxy)
            time.sleep(1)  # Пауза 1 секунда между запусками потоков
        else:
            print("Вне заданного времени работы (2:00–6:00 по Киеву). Ожидание...")
            time.sleep(60)  # Проверка времени раз в минуту
