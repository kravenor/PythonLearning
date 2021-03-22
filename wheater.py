import requests, json
city='Montepulciano'
api_key="YOUR_API_KEY"
base_url="https://api.openWeathermap.org/data/2.5/weather?"
url=base_url+"appid="+api_key+"&q="+city
response=requests.get(url)
x=response.json()
print(x)
if x['cod']!=401:
    print("city Name: ",x['name'])
    print("Wheater: ",x['weather'])
    print("Wheater: ",x['weather'][0]['main'])
    print("Temp: ",x['main']['temp'])
    print("Minimum Temp: ",x['main']['temp_min'])
    print("Maximum Temp: ",x['main']['temp_max'])
else:
    print('City not found')