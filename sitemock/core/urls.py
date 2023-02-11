from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]

handler404 = 'sitemock.core.views.error_404_view'