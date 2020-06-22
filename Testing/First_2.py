import requests

response = requests.get('https://api.github.com')
#print(response.content)  # получаем содержимое payload в байтах
response.encoding = 'utf-8'  # указывем конкретную кодировку
print(response.text)  # конвертация инфы в строку UTF-8

print(response.json())

