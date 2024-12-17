TEST_URL = "http://httpbin.org/ip"

def test_proxy():
    for proxy in PROXIES_LIST:
        try:
            print(f"Проверка прокси: {proxy['http']}")
            response = requests.get(TEST_URL, proxies=proxy, timeout=10)
            print(f"Ответ: {response.json()}")
        except Exception as e:
            print(f"Ошибка: {e}")

test_proxy()
