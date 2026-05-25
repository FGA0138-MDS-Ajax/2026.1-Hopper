from django.urls import path
<<<<<<< HEAD

from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("callback/", views.callback_view, name="callback"),
    path("logout/", views.logout_view, name="logout"),
]
=======
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
]
>>>>>>> feature/usuarios-urls
