from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
from datetime import datetime

# URL для посещения
URL = "https://webdesign-finder.com/cogniart/404"

# Настройка прокси
PROXIES_LIST = [
    "hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001",
    "hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002",
    "hFPncvbbuc_2:22VnEeaqTBFI@s-17704.sp6.ovh:11003",
]

# Путь к Chromedriver на Heroku
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
GOOGLE_CHROME_SHIM = "/app/.apt/usr/bin/google-chrome"

def visit_site(proxy):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Настройка параметров Chrome
        chrome_options = Options()
        chrome_options.binary_location = GOOGLE_CHROME_SHIM
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument(f"--proxy-server=http://{proxy}")

        # Запуск Chrome
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        print(f"[{now}] Пытаюсь посетить сайт через прокси: {proxy}")
        driver.get(URL)

        if "404" not in driver.page_source:
            print(f"[{now}] Сайт успешно посещён через {proxy}")
        else:
            print(f"[{now}] Ошибка: Страница не загружена корректно.")

        driver.quit()
    except Exception as e:
        print(f"[{now}] Прокси {proxy} не сработал. Ошибка: {e}")

# Планировщик
def scheduler():
    while True:
        now = datetime.now()
        if 2 <= now.hour < 5:
            for proxy in PROXIES_LIST:
                visit_site(proxy)
                time.sleep(3)
        else:
            print(f"[{now}] Время вне диапазона, ожидание...")
            time.sleep(60)

if __name__ == "__main__":
    scheduler()
