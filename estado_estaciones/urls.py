from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from estado_estaciones import views

router = DefaultRouter()

router.register(r'estados-estacion', views.Lista_estado_estaciones, basename='estados-estaciones')


urlpatterns=[
    
    path('', include(router.urls)),

]