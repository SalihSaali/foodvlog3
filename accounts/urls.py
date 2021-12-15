from django.urls import path
from.import views


urlpatterns = [
    path('Register',views.register,name='Register'),
    path('Login',views.login_view,name='Login'),
    path('Logout',views.logout_view,name='Logout'),
    ]