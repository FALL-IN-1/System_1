from django.urls import path
from . import views

urlpatterns = [
    path('',views.every_place, name='khawar_place'),

]