import requests

response = requests.get('https://api.github.com')

print(response.json())  # получаем в виде словаря данные

print(response.headers)  # просмотр HTTP заголовков, возвращает словарь

print(response.headers['Content-Type'])


