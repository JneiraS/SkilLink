from django.urls import path

from . import views

app_name = 'mutual_support'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('offers-form/', views.offers_form_view, name='offers_form'),
    path('request-form/', views.assistance_request_view, name='request_form'),
    path('offer/<int:creneau_id>/', views.offer_view, name='offer'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
]
