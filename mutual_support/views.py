from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from django.shortcuts import render, redirect, get_object_or_404

from mutual_support.forms import CreneauForm
from mutual_support.models import Competence, Creneau, UserCompetence, Profile
from mutual_support.src.api import WeatherAPI
from mutual_support.src.time_stamping import APITimestamp

INDEX_PAGE = 'mutual_support:index'
api_data = WeatherAPI('Soustons', '111a7cf74496e5693e3fcd124fb4947d')
stamp = APITimestamp(api_data)


def index(request):
    """vue pour la page d'accueil qui affiche une liste de categories
    distinctes et toutes les offres disponibles, triées par date.
    """
    rainy_days: set = WeatherAPI.get_rainy_days(stamp.get_data())
    offers = Creneau.objects.filter(~Q(user=request.user.id)).order_by('date')
    categories: QuerySet = Competence.objects.values_list('category', flat=True).distinct()

    Creneau.set_rainy_status(offers, rainy_days)

    context = {
        'categories': categories,
        'offers': offers,
        'rainy_days': rainy_days,
    }
    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username.strip(), password=password)
        if user is not None:
            login(request, user)
            return redirect(INDEX_PAGE)
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect"
    else:
        error_message = ""

    return render(request, 'login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect(INDEX_PAGE)


def signup(request):
    """ Vue pour la page de formulaire d'inscription.
    avec création d'un profil vide associé."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Création d'un nouveau profil pour l'utilisateur avec des valeurs par défaut
            Profile.objects.create(user=user)
            # Extraction du nom d'utilisateur et du mot de passe de la donnée nettoyée du formulaire
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authentification de l'utilisateur avec le nom d'utilisateur et le mot de passe fournis
            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect(INDEX_PAGE)
    else:

        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def offer_view(request, creneau_id):
    offer = get_object_or_404(Creneau, pk=creneau_id)
    if request.method == 'POST':
        offer.is_reserved = True
        offer.save()
        return redirect(INDEX_PAGE)
    return render(request, 'offer-details.html', {'creneau': offer})


@login_required(login_url="/login/")
def offers_form_view(request):
    if request.method == 'POST':
        form = CreneauForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form.instance.user = current_user
            form.save()
            return redirect(INDEX_PAGE)
    else:
        form = CreneauForm()

    return render(request, 'offers-form.html', {'form': form})


@login_required(login_url="/login/")
def assistance_request_view(request):
    if request.method == 'POST':
        form = CreneauForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form.instance.user = current_user
            form.instance.is_help_offered = False
            form.save()
            return redirect(INDEX_PAGE)
    else:
        form = CreneauForm()

    return render(request, 'assistance_request-form.html', {'form': form})


@login_required(login_url="/login/")
def profile_view(request, user_id):
    user_profile = get_object_or_404(User, pk=user_id)
    user_competences = UserCompetence.objects.filter(user=user_id)
    interesting_requests = Creneau.objects.filter(
        competence__in=user_competences.values_list('competence', flat=True))

    context = {'profile_user': user_profile, 'competences': user_competences,
               "interesting_requests": interesting_requests}

    return render(request, 'profile.html', context)


def category_view(request, category_slug):
    """
    Vue qui affiche les offres pour une catégorie spécifique.
    """
    category = category_slug.replace('-', ' ').strip()
    offers = Creneau.objects.filter(competence__category=category).order_by('date')
    context = {'offers': offers, 'category': category}
    return render(request, 'categories.html', context)


def competences(request):
    """
    Vue qui affiche la liste de toutes les compétences.
    """
    list_competences = Competence.objects.all()
    return render(request, 'competences.html', {'competences': list_competences})
