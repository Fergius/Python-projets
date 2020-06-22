import requests

response = requests.get('https://api.github.com')

# Проверка на код
if response.status_code == 200:
    print("Success")
elif response.status_code == 404:
    print('Not Found')

# Более общая проверка на код в промежутке от 200 до 400
if response:
    print('Success')
else:
    print('An error has occured')
    