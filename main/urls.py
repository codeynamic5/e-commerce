from django.urls import path
from main.views import show_main, show_model_main, show_static_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('model/', show_model_main, name='show_model_main'),
    path('static/', show_static_main, name='show_static_main'),
]