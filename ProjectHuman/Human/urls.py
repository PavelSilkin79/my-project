from django.contrib import admin
from django.urls import path


from Human.views import index, get_profession, view_human, add_human


urlpatterns = [
     path('', index, name='Home'),
     path('profession/<int:profession_id>/', get_profession, name='Profession'),
     path('human/<int:human_id>/', view_human, name='View_human'),
     path('human/add_human', add_human, name='Add_human'),
]



