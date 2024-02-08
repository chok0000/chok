from django.urls import path
from app_chok import views
urlpatterns=[

    path('',views.index),
    path('about',views.about),
    path('gallery',views.gallery),
   
]