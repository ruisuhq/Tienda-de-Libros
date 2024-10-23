import requests
from django.shortcuts import render

def book_list(request):
    query = request.GET.get('q', 'Steven Universe')
    api_key = 'AIzaSyBw_Lx0hqF-HYDSeER3kEpF4OPjZGGfrGI' 
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}&maxResults=10'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        books = response.json().get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Google Books API: {e}")
        books = []
    
    return render(request, 'bookstore/index.html', {'books': books, 'query': query})
