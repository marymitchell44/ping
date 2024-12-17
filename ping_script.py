import requests
import time
from itertools import cycle
from datetime import datetime

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

# Список прокси
PROXIES = [
    {"http": "http://hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001",
     "https": "http://hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001"},
    {"http": "http://hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002",
     "https": "http://hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002"},
    {"http": "http://hFPncvbbuc_2:22VnEeaqTBFI@s-17704.sp6.ovh:11003",
     "https": "http://hFPncvbbuc_2:22VnEeaqTBFI@s-17704.sp6.ovh:11003"},
    {"http": "http://hFPncvbbuc_3:22VnEeaqTBFI@s-17704.sp6.ovh:11004",
     "https": "http://hFPncvbbuc_3:22VnEeaqTBFI@s-17704.sp6.ovh:11004"},
    {"http": "http://hFPncvbbuc_4:22VnEeaqTBFI@s-17704.sp6.ovh:11005",
     "https": "http://hFPncvbbuc_4:22VnEeaqTBFI@s-17704.sp6.ovh:11005"},
    {"http": "http://hFPncvbbuc_5:22VnEeaqTBFI@s-17704.sp6.ovh:11006",
     "https": "http://hFPncvbbuc_5:22VnEeaqTBFI@s-17704.sp6.ovh:11006"},
    {"http": "http://hFPncvbbuc_6:22VnEeaqTBFI@s-17704.sp6.ovh:11007",
     "https": "http://hFPncvbbuc_6:22VnEeaqTBFI@s-17704.sp6.ovh:11007"},
    {"http": "http://hFPncvbbuc_7:22VnEeaqTBFI@s-17704.sp6.ovh:11008",
     "https": "http://hFPncvbbuc_7:22VnEeaqTBFI@s-17704.sp6.ovh:11008"},
    {"http": "http://hFPncvbbuc_8:22VnEeaqTBFI@s-17704.sp6.ovh:11009",
     "https": "http://hFPncvbbuc_8:22VnEeaqTBFI@s-17704.sp6.ovh:11009"},
    {"http": "http://hFPncvbbuc_9:22VnEeaqTBFI@s-17704.sp6.ovh:11010",
     "https": "http://hFPncvbbuc_9:22VnEeaqTBFI@s-17704.sp6.ovh:11010"}
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
        if 1 <= current_hour < 5:
            proxy = next(proxy_pool)
            visit_site(proxy)
            time.sleep(2)  # Пауза 2 секунды между запросами
        else:
            print("Вне заданного времени работы (3:00–7:00 по Киеву). Ожидание...")
            time.sleep(60)  # Проверка времени раз в минуту
