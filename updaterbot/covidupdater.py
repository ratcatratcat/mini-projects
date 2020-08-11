import requests
from win10toast import ToastNotifier
import json
import time


def update():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = f'Conirmed Cases: {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates", text, duration= 10)
        time.sleep(3600)


update()
