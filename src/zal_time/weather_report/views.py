from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
import requests

CITIES = [
    "New+York", "London", "Tokyo", "Paris", "Sydney", 
    "Dubai", "Mumbai", "Cape+Town", "Toronto", "Los+Angeles", 
    "Beijing", "Moscow", "Rio+de+Janeiro", "Berlin", "Singapore", 
    "Mexico+City", "Istanbul", "Seoul", "Bangkok", "Buenos+Aires",
    "Tehran"
] * 3


def get_weather(request):
    def get_city_weather():
        yield f"CITY,feals_like_c,feals_like_f,temp_c,temp_f,cloud_cover,humidaty\n"
        for city in CITIES:
            response = requests.get(f"https://wttr.in/{city}?format=j1")
            data = response.json()
            feals_like_c = data["current_condition"][0]["FeelsLikeC"]
            feals_like_f = data["current_condition"][0]["FeelsLikeF"]
            temp_c = data["current_condition"][0]["temp_C"]
            temp_f = data["current_condition"][0]["temp_F"]
            cloud_cover = data["current_condition"][0]["cloudcover"]
            humidaty = data["current_condition"][0]["humidity"]

            yield f"{city},{feals_like_c},{feals_like_f},{temp_c},{temp_f},{cloud_cover},{humidaty}\n"

    response = StreamingHttpResponse(get_city_weather(), content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="simple_data.csv"'


    return response
