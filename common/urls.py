from django.urls import path
from django.contrib.auth import views as auth_viewws

app_name = 'common'

urlpatterns = [
    path('login/', auth_viewws.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_viewws.LogoutView.as_view(), name='logout')
]