from django.urls import path
from . import views


#app_name = "RioolApp"
urlpatterns = [
    path("", views.landing, name="landing"),
    path('nieuw_model/', views.nieuw_model, name='nieuw_model'),
    path('overzicht/', views.overzicht, name='overzicht'),
    path('meerjarenplanning/', views.meerjarenplanning, name='meerjarenplanning'),
    path('meerjarenplanning/standaard_beoordeling', views.standaard_beoordeling, name='standaard_beoordeling'),

]