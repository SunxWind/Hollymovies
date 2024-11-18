"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viewer.views import hello, index, MovieCreateView, MovieView, GenreCreateView, GenreView, ActorCreateView, ActorView, ActorUpdateView, CustomLoginView, ProfileView, RegisterView, MovieUpdateView
from viewer.models import Genre, Movie
from django.contrib.auth import views


admin.site.register(Genre)
admin.site.register(Movie)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<value>', hello, name='hello'),
    path('', index, name='index'),

    path('movies', MovieView.as_view(), name='movies'),
    path('movie_add', MovieCreateView.as_view(), name='movie_add'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),

    path('genres', GenreView.as_view(), name='genres'),
    path('genre_add', GenreCreateView.as_view(), name='genre_add'),

    path('actors', ActorView.as_view(), name='actors'),
    path('actor', ActorCreateView.as_view(), name='actor_add'),
    path('actor/update/<pk>', ActorUpdateView.as_view(), name='actor_update'),

    path('login', CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile')
]
