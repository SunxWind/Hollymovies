from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, ListView, TemplateView, UpdateView
from viewer.forms import MovieForm, GenreForm, ActorForm, SignUpForm
from viewer.models import Movie, Genre, Actor
from django.urls import reverse_lazy


# Create your views here.
def hello(request, value):
    return HttpResponse(f"Hello world! {value}")


def index(request):
    value = request.GET.get('value', '')
    return render(request, template_name='index.html', context={'hodnota': value})


def login(request):
    # value = request.GET.get('value', '')
    return render(request, template_name='login.html')# , context={'hodnota': value})


# def register(request):
#     # value = request.GET.get('value', '')
#     return render(request, template_name='register.html')# , context={'hodnota': value})

"""
def movie_add(request):
    # value = request.GET.get('value', '')
    form = MovieForm()
    return render(request, template_name='movie_add.html', context={'form': form})
"""
class ProfileView(TemplateView):
    template_name = 'profile.html'


class CustomLoginView(LoginView):
    template_name ='registration/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class MovieView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description']
        )
        return result

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/movies')
        return super().dispatch(request, *args, **kwargs)


class GenreView(ListView):
    template_name = "genres.html"
    model = Genre


class GenreCreateView(FormView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name=cleaned_data['name'],
        )
        return result


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('movies')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/movies')
        return super().dispatch(request, *args, **kwargs)


class ActorView(ListView):
    template_name = "actors.html"
    model = Actor


class ActorCreateView(FormView):
    template_name = 'actor_form.html'
    form_class = ActorForm
    success_url = reverse_lazy('actors')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Actor.objects.create(
            firstname=cleaned_data['firstname'],
            lastname=cleaned_data['lastname'],
            birth_date=cleaned_data['birth_date']
        )
        return result

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/actors')
        return super().dispatch(request, *args, **kwargs)


class ActorUpdateView(UpdateView):
    template_name = 'actor_form.html'
    form_class = ActorForm
    model = Actor
    success_url = reverse_lazy('actors')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/actors')
        return super().dispatch(request, *args, **kwargs)