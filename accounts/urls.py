from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .views import signup, mypage

urlpatterns = [
    url(r'^mypage/$', mypage, name='account.mypage'),
    url(r'^signup/$', signup, name='account.signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='account.logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'),
        name='account.login'),
    url(r'^password/$', 
        auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='account.password_change'),
    url(r'^password/done/$', 
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
]
