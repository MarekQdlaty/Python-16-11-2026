# REST API
# Swagger
# https://swagger.io
# Informacje o naszych reklamach
# Api Programming - API Tool For Developers
# Sponsorowane
# Optimize API development with unified workflows, multi-protocol support & easy integration.
# Swagger's architecture enables seamless cross-team collaboration on API design and docs.
#
#

# A REST API (Representational State Transfer API) is a web API that follows REST architectural
# constraints, using standard HTTP methods like GET, POST, PUT,
# and DELETE to access and manipu
# late resources identified by URLs.

# klient http
# httpx, niquests
import requests

# pip install requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)
# <Response [200]>
# 200 ok
# 3xx - warningi
# 404 - brak strony, 400  Bad Request
# 5xx 500 Interna Server Error

print(response.text)

data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A',
# 'currency': 'dolar amerykański',
# 'code': 'USD',
# 'rates': [{'no': '226/A/NBP/2026', 'effectiveDate': '2026-11-20', 'mid': 4.0613}]}

# nazwa i kurs