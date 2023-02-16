from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("contact/", views.contact, name="contact"),
    path("user/dashboard/", views.dashboard, name="dashboard"),
    path("user/edit/", views.edit_user, name="edit_user"),
    path("user/editar-senha/", views.edit_passwd, name="edit_passwd"),
    path("password_reset", views.password_reset_request, name="password_reset"),
]

handler404 = 'sitemock.core.views.error_404_view'
