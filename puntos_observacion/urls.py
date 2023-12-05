from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from puntos_observacion import views

router = DefaultRouter()
router.register(r'puntos-observacion', views.GetAllPuntoObservacion,basename='puntos-observacion')
router.register(r'puntos-observacion', views.GetIdPuntoObservacion,basename='puntos-observacion')
router.register(r'puntos-observacion', views.insertarPunto,basename='puntos-observacion')
router.register(r'puntos-observacion', views.GetCodigo,basename='puntos-observacion')



urlpatterns=[
    
    path('', include(router.urls)),

]