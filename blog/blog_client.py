import requests




data = {
    'details':'aowidnawo inawo i0',
    'age':32,
    'language':'Engawd'
        }
url = 'http://localhost:8000/blogs/create'
url2 = 'http://localhost:8000/blogs/list'


res = requests.post(url=url,data=data)
# res2 = requests.get(url=url2)
print(res.status_code)
print(res.text)

# print(res2.status_code)
# print(res2.text)