from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_to_external_website2),
    path('<path:my_path>/', redirect_to_external_website)
]
