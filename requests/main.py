import requests
"""
params = {"q": "pizza"}

r = requests.post("http://bing.com/search", params=params)
print("Status:", r.status_code)
print(r.url)

f = open("./page.html", "w+")
f.write(r.text)
"""
my_data = {"name": "Babajaga", "email": "babajaga@example.com"}

r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)
print("Status:", r.status_code)
print(r.url)

f = open("./myfile.html", "w+")
f.write(r.text)