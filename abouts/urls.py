from django.urls import path
from . views import abouts_list

app_name = 'abouts'

urlpatterns = [
    path('abouts/', abouts_list, name='abouts_list')
    
]



