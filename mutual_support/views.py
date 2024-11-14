from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from mutual_support.forms import CreneauForm
from mutual_support.models import Competence, Creneau, UserCompetence, Profile

INDEX_PAGE = 'mutual_support:index'


def index(request):
    """vue pour la page d'accueil qui affiche une liste de categories
    distinctes et toutes les offres disponibles, triées par date.
    """
    categories = Competence.objects.values_list('category', flat=True).distinct()
    offers = Creneau.objects.all().order_by('date')
    index_competences = Competence.objects.all()
    context = {
        'categories': categories,
        'offers': offers,
        'competences': index_competences

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

    return render(request, 'offers-form.html', {'form': form})  # The form variable is used here


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

    return render(request, 'assistance_request-form.html', {'form': form})  # The form variable is used here


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
    competences = Competence.objects.all()
    return render(request, 'competences.html', {'competences': competences})
