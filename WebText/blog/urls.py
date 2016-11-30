from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^register$', views.UserRegister, name='register'),
    url(r'^$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^index/add/$', views.create_blog, name='add_blog'),
]