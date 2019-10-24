import requests

url = 'https://api.chucknorris.io/jokes/KHxl9OXyRN6zaQYvCLZfow'
r = requests.get(url)
print("Status code",r.status_code)

response_dict = r.json()

print(response_dict.keys())
