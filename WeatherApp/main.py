import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=30e9bc50dc6040efbc4175730242301&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
print(f"Temperature in {city} is " + str(wdic["current"]["temp_c"]) + " C")
engine = pyttsx3.init()
engine.say(f"Temperature in {city} is {wdic["current"]["temp_c"]} degree celcius")
engine.runAndWait()
