from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<str:book_id>/', views.book_detail, name='book_detail'),
    path('book/<str:book_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
