import requests
import time

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

# Функция для посещения страницы
def visit_site():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            print("done")
        else:
            print(f"error: Код ответа {response.status_code}")
    except Exception as e:
        print(f"error: {e}")

# Бесконечный цикл
if __name__ == "__main__":
    while True:
        visit_site()
        time.sleep(60)  # Пауза 60 секунд между запросами
