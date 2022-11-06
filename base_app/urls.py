from django.urls import path
from .views import all_doner_blood_group,search_blood_group,Home

urlpatterns = [
    path('', Home ,name='Home'),
    path('all_blood_group/', all_doner_blood_group,name='all_doner_blood_group'),
    path('blood_group_search/', search_blood_group,name='search_blood_group'),
    path('blood_group_search/<int:page>/', search_blood_group,name='search_blood_group')


]