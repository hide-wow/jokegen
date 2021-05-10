import requests
import json
from time import sleep

url = "https://api.blablagues.net/?rub=blagues&?cat=jeu+de+mots,devinettes,histoires+droles&?nb=1"
data = requests.get(url).content.decode('utf-8')
values = json.loads(data)
doto = values["data"]
content = doto["content"]
joke = content["text_head"]
jspcoik = content["text"]
responce = content["text_hidden"]

print(joke)
print(jspcoik)
print(responce)

sleep(10000.0)