from django.urls import path

from buyer import views

urlpatterns=[
    path('',views.first,name = 'buyyer_page')
]