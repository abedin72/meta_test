from django.urls import path
from .import views

app_name='accounts'
urlpatterns = [
    path('accounts/login/',views.login,name='login'),
    path('accounts/logout/',views.logout,name='logout'),
    path('accounts/profile/',views.profile,name='profile'),
    path('accounts/register/',views.register,name='register'),
    path('accounts/profileRegister/',views.profileRegister,name='profileRegister'),
]
