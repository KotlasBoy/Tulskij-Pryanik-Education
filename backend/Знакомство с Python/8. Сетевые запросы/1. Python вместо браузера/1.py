import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)

print(response.text)  # напечатайте текст HTTP-ответа