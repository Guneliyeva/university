from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import University
import requests

# Create your views here.

def search_universities(request):
    query = request.GET.get('query', '')
    if query:
        url = f"https://www.example.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Örnek olarak, belirli bir HTML yapıdan verileri çekme
        universities = soup.find_all('div', class_='university')
        for uni in universities:
            name = uni.find('h2').text
            url = uni.find('a')['href']
            University.objects.create(name=name, url=url)
    
    results = University.objects.all()
    return render(request, 'index.html', {'results': results})
