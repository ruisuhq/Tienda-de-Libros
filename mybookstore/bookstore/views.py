import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EditProfileForm

def book_list(request):
    query = request.GET.get('q', 'Minecraft')
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

def book_detail(request, book_id):
    api_key = 'AIzaSyBw_Lx0hqF-HYDSeER3kEpF4OPjZGGfrGI'
    api_url = f'https://www.googleapis.com/books/v1/volumes/{book_id}?key={api_key}'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        book = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching book details from Google Books API: {e}")
        book = None
    
    return render(request, 'bookstore/book_detail.html', {'book': book})

def add_to_cart(request, book_id):
    # Aquí puedes implementar tu lógica para añadir el libro al carrito (usando la sesión o la base de datos)
    book = requests.get(f'https://www.googleapis.com/books/v1/volumes/{book_id}').json()
    
    # Imaginemos que usamos la sesión para almacenar el carrito:
    cart = request.session.get('cart', [])
    cart.append(book)
    request.session['cart'] = cart
    
    return redirect('book_detail', book_id=book_id)

@login_required
def profile_view(request):
    return render(request, 'bookstore/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'bookstore/edit_profile.html', {'form': form})