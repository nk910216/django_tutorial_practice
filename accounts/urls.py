from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .views import signup

urlpatterns = [
    url(r'^signup/$', signup, name='account.signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='account.logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), 
        name='account.login'),
]
