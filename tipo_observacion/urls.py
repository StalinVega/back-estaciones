from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from tipo_observacion import views

router = DefaultRouter()
router.register(r'tipo-observacion', views.GetAllListaObservacion,basename='tipo-observacion')

urlpatterns=[
    
    path('', include(router.urls)),

]