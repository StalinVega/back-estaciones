from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from ubicacion import views

router = DefaultRouter()
router.register(r'provincias', views.GetAllProvince,basename='provincia')
router.register(r'cantones', views.View_Canton,basename='cantones')
router.register(r'cuencas', views.View_Cuenca,basename='cuencas')
router.register(r'parroquias', views.View_Parroquia,basename='parroquia')
urlpatterns=[
    
    path('', include(router.urls)),

]