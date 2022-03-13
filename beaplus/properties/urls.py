"""Properties URLs."""

# Django
from django.urls import path

# Views
from beaplus.properties import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        route='properties/<int:pk>/',
        view=views.PropertyDetailView.as_view(),
        name='detail'
    ),
    
]