from django.urls import path

from base import views

app_name = 'base'
urlpatterns = [

    path("", views.index, name="index"),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

]
