TEST_URL = "http://httpbin.org/ip"
PROXIES_LIST = [
    {"http": "http://hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001",
     "https": "https://hFPncvbbuc_0:22VnEeaqTBFI@s-17704.sp6.ovh:11001"},
    {"http": "http://hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002",
     "https": "https://hFPncvbbuc_1:22VnEeaqTBFI@s-17704.sp6.ovh:11002"},
    {"http": "http://hFPncvbbuc_2:22VnEeaqTBFI@s-17704.sp6.ovh:11003",
     "https": "https://hFPncvbbuc_2:22VnEeaqTBFI@s-17704.sp6.ovh:11003"},
]

def test_proxy():
    for proxy in PROXIES_LIST:
        try:
            print(f"Проверка прокси: {proxy['http']}")
            response = requests.get(TEST_URL, proxies=proxy, timeout=10)
            print(f"Ответ: {response.json()}")
        except Exception as e:
            print(f"Ошибка: {e}")

test_proxy()
