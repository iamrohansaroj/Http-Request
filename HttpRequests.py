import requests

r = requests.get("https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=d44e6dc5d622b2ff97fa28b383069a4e")
print(r.text)
print(r.status_code)

url = "https://www.google.com/"
data = {
    "username":7,
    "password":7722
}
r2 = requests.post(url=url, data=data)
print(r.text)