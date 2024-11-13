from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from mutual_support.forms import CreneauForm
from mutual_support.models import Competence, Creneau

INDEX_PAGE = 'mutual_support:index'


def index(request):
    categories = Competence.objects.values_list('category', flat=True).distinct()
    offers = Creneau.objects.all().order_by('date')
    current_user = request.user
    print(offers[0].competence)
    context = {
        'categories': categories,
        'offers': offers
    }
    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(INDEX_PAGE)
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(INDEX_PAGE)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(INDEX_PAGE)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def offers_form_view(request):
    if request.method == 'POST':
        form = CreneauForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form.instance.user = current_user
            form.save()
            return redirect(INDEX_PAGE)
    else:
        form = CreneauForm()  # This line is not the issue

    return render(request, 'offers-form.html', {'form': form})  # The form variable is used here
