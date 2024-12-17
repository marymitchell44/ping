import requests

# URL для посещения
URL = "http://webdesign-finder.com/cogniart"

# Функция для посещения страницы
def visit_site():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            print("done")  # Успешный ответ
        else:
            print(f"error: Код ответа {response.status_code}")  # Ответ с ошибкой
    except Exception as e:
        print(f"error: {e}")  # Ошибка при запросе

# Запуск функции
if __name__ == "__main__":
    visit_site()
