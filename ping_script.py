import requests
import time
from datetime import datetime

# URL для посещения
URL = "https://webdesign-finder.com/cogniart/404"

# Заголовки для имитации реального браузера
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Функция для посещения сайта
def visit_site():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Определяем время перед try
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            print(f"[{now}] Сайт успешно посещён. Код ответа: {response.status_code}")
        else:
            print(f"[{now}] Ошибка при посещении сайта. Код ответа: {response.status_code}")
    except Exception as e:
        print(f"[{now}] Ошибка: {e}")

# Планировщик: запуск каждую 3 секунды с 2 до 5 утра
def scheduler():
    while True:
        now = datetime.now()
        # Проверяем, если текущее время между 2:00 и 5:00 утра
        if 2 <= now.hour < 5:
            visit_site()
            time.sleep(3)  # Пауза на 3 секунды
        else:
            print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Время вне диапазона, ожидание...")
            time.sleep(60)  # Проверка раз в минуту

# Запуск планировщика
if __name__ == "__main__":
    scheduler()
