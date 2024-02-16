from django.urls import path
from celery_home import views

urlpatterns = [
    path('' , views.home , name='index'),
    path('about/' , views.about , name='about'),
    path('contact/' , views.contact , name='contact'),

]
