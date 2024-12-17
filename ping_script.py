from dotenv import load_dotenv
import os
import requests
import time
from itertools import cycle
from datetime import datetime

# Загрузка переменных из файла .env
load_dotenv()

# URL для посещения
URL = "http://webdesign-finder.com/cogniart"

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
def visit_site(proxy):
    try:
        print(f"Посещение сайта через прокси: {proxy['http']}")
        response = requests.get(URL, headers=HEADERS, proxies=proxy, timeout=10)
        if response.status_code == 200:
            print("done")
        else:
            print(f"error: Код ответа {response.status_code}")
    except Exception as e:
        print(f"error: {e}")

# Основной цикл с проверкой времени
if __name__ == "__main__":
    while True:
        # Получаем текущее серверное время (UTC)
        current_hour = datetime.utcnow().hour

        # Проверяем, что время между 1:00 и 5:00 UTC (3:00–7:00 по Киеву)
        if 0 <= current_hour < 6:
            proxy = next(proxy_pool)
            visit_site(proxy)
            time.sleep(2)  # Пауза 2 секунды между запросами
        else:
            print("Вне заданного времени работы (3:00–7:00 по Киеву). Ожидание...")
            time.sleep(60)  # Проверка времени раз в минуту
