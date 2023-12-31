from django.urls import path, include
from .views import home, filter_data

urlpatterns = [
    path('', home, name='home'),
    path('filter-data/', filter_data, name='filter-data'),

]
