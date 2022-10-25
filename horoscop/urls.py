from django.urls import path
from . import views

urlpatterns = [
    path('horoscope/<sign_zodiac>/', views.get_info_zodiac, name='horoscope-name'),
    path('horoscope/', views.get_main_paige, name='horoscope-main'),
]
