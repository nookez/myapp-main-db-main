from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from .views import signup_view
from .views import add_user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('movie/<int:id>/', views.toppick, name='toppick'),
    path('coming-soon/<int:id>/', views.coming_soon_detail, name='coming_soon_detail'),
    path('celebrity/<int:id>/', views.celebrity_detail, name='celebrity_detail'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('search/', views.search_movies, name='search_movies'),
    path('signup/', signup_view, name='signup'),
    path('add-user/', add_user_view, name='addUser'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('success/', views.success_view, name='success_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
