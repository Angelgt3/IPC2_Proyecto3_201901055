from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Login),
    path('principal/', views.Principal),
    path('principal/consulta/',views.Consu),
    path('principal/informacion/',views.Info),
    path('principal/documentacion/',views.Doc),
    path('principal/filtrar/',views.Filtros),
    path('principal/filtrarC/',views.Filtro2),
]