"""Python Requests параметры запроса"""

import requests

# поиск местонахождения для запросов на Github
response = requests.get('https://api.github.com/search/repositories',
                        params={'q': 'requests+language:python'})

# Анализ некоторых атрибутов местонахождения запросов

json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')