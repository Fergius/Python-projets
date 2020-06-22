"""Примеры HTTP методов в Requests"""
import requests

print(requests.post('https://httpbin.org/post', data={'key': 'value'}))
print(requests.put('https://httpbin.org/post', data={'key': 'value'}))
print(requests.delete('https://httpbin.org/delete'))
print(requests.head('https://httpbin.org/get'))
