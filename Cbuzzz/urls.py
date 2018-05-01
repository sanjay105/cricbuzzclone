from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    #path('', views.index, name='index'),

]