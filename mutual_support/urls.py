from django.urls import path

from . import views

app_name = 'mutual_support'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.signup, name='signup')
]
