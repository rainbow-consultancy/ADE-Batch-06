# Wheather API 

# import requests

# # city = input("Enter the city name: ")
# api_token = "23c7abd85fd57c0868a9f281f80e8911"
# url_token = "https://api.openweathermap.org/assistant/session"


# def get_whether_summery() -> str:
#     headers = {
#         "Content-Type": "application/json",
#         "X-Api-Key": api_token
#     }
    
#     data = {
#         "prompt": "What’s weather like in London?"
#     }
    
#     response = requests.post(url_token, headers=headers, json=data)
    
#     print(response.json())


# get_whether_summery()



import requests

city = input("Enter the City name: ")
api_key = "23c7abd85fd57c0868a9f281f80e8911"


def get_weather_report(city: str, api_key: str) -> str:
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    data = response.json()
    # print(data)
    res = f"{city} temperature is: {round(data["main"]["temp"])}"
    return res

print(get_weather_report(city, api_key))
    