import os, json
import requests
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

apikey=os.getenv("openai_key_speech")
endpoint=os.getenv("endpoint_speech")
weather_api=os.getenv("weather_api")

city_name=input("Enter the city to check weather : ")
def main():
    client=AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=apikey,
        api_version="2024-02-01"
    )
    functions=[
        {
        "name":"getWeather",
        "description":"Retrive real-time weather information/data about a particular loacation/place",
        "parameters":{
            "type":"object",
            "properties":{
                "location":{
                    "type":"string",
                    "description":"the excat location whose real-time weather is to be determined",
                },
            },
            "required":["location"]
        },
        }
    ]
    
    initial_response=client.chat.completions.create(
        model=os.getenv("chat_model"),
        messages=[
            {"role":"system","content":"You are an assistant that helps people retrive real-time weather data/info"},
            {"role":"user","content":f"How is weather in {city_name}?"}
        ],
        functions=functions
    )
    
    function_argument=json.loads(initial_response.choices[0].message.function_call.arguments)
    location=function_argument['location']
    if location:
        print(f"city : {location}")
        get_weather(location)
        
def get_weather(location):
    url="https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + str(weather_api)
    response=requests.get(url)
    get_response=response.json()
    lattitude=get_response["coord"]["lat"]
    longitude=get_response["coord"]["lon"]
    print(f"lattitude : {lattitude}")
    print(f"longitude : {longitude}")
    
    url_final="https://api.openweathermap.org/data/2.5/weather?lat=" + str(lattitude) + "&lon=" + str(longitude) + "&appid=" + str(weather_api)
    final_response=requests.get(url_final)
    final_response_json=final_response.json()
    weather=final_response_json["weather"][0]["description"]
    print(f"weather condition : {weather}")
    
if __name__=='__main__':
    main()
    
    




