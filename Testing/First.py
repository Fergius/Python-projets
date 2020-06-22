import requests

response = requests.get('https://api.github.com')
print(response) # получение статус кода в виде <response [200]>
print(response.status_code) # Получение статус кода 200

