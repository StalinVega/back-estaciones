from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from estaciones import views

router = DefaultRouter()

router.register(r'estaciones', views.Busca_Estaciones, basename='estaciones')
router.register(r'estaciones', views.Lista_Estaciones, basename='estaciones')
router.register(r'estaciones', views.GetIdEstacion, basename='estaciones')

urlpatterns=[
    
    path('', include(router.urls)),

]