from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from tipo_estacion import views

router = DefaultRouter()
router.register(r'tipos-estacion', views.GetAllTypeStations,basename='tipos-observacion')

urlpatterns=[
    
    path('', include(router.urls)),

]