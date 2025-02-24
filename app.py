from flask import *
import requests

app = Flask(__name__)

url = "https://lager.emilfolino.se/v2/products/everything"
response = requests.get(url)
products_dict = response.json()

summed_products = {}
unique_names = []


for i in products_dict["data"]:
    if type(i["stock"]) is int:
        if i["name"] not in unique_names:
            summed_products.update({str(i["name"]): int(i["stock"])})
        else:
            summed_products.update({i["name"]: summed_products[i["stock"]] + i["stock"]})

jsoned = { "data": []}

for i in summed_products:
    jsoned["data"].append({"name": i, "stock": summed_products[i]})



@app.route("/")
def home():
    return redirect("/unique")

@app.route("/unique")
def unique():
    return jsoned  

@app.route("/search/<query>")
def search(query):
    match = {"data": []}
    for i in jsoned["data"]:
        if query in i["name"]:
            match["data"].append(i)
    return match
























