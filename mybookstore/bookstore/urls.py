from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<str:book_id>/', views.book_detail, name='book_detail'),
    path('book/<str:book_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('login/', LoginView.as_view(template_name='bookstore/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)