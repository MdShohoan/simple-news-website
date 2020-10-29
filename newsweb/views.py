from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=759a41ef0f944f91a5939ea831376dd8")
    api = json.loads(news_api_request.content)

    return render(request, 'home.html', {'api': api})