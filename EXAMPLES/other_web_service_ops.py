#!/usr/bin/env python
import requests

print('PUT:')
r = requests.put("http://httpbin.org/put", data={'spam': 'ham'}) # <1>
print(r.status_code, r.text)
print('-' * 60)

print('PATCH:')
r = requests.patch("http://httpbin.org/patch", data={'spam': 'ham'}) # <1>
print(r.status_code, r.text)
print('-' * 60)


print('DELETE:')
r = requests.delete("http://httpbin.org/delete") # <2>
print(r.status_code, r.text)
print('-' * 60)

print('HEAD:')
r = requests.head("http://httpbin.org/get") # <3>
print(r.status_code, r.text)
print(r.headers)
print('-' * 60)

print('OPTIONS:')
r = requests.options("http://httpbin.org/get") # <4>
print(r.status_code, r.text)
print('-' * 60)

