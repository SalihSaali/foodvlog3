from django.urls import path
from.import views


urlpatterns = [
    path('Register',views.register,name='Register'),
    path('Login',views.login,name='Login'),
    path('Logout',views.logout,name='Logout'),
    ]