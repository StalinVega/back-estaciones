from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from puntos_observacion import views

router = DefaultRouter()
router.register(r'puntos-observacion', views.GetAllPuntoObservacion,basename='puntos-observacion')
router.register(r'puntos', views.GetIdPuntoObservacion,basename='puntos')
router.register(r'ingreso', views.insertarPunto,basename='ingreso')



urlpatterns=[
    
    path('', include(router.urls)),

]