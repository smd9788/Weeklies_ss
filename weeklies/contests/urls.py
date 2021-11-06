from django.urls import path
from . import views

urlpatterns = [
    path('api/contest/', views.ContestListCreate.as_view() ),
]