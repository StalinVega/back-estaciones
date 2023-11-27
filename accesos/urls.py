from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from accesos import views

router = DefaultRouter()
router.register(r'accesos', views.GetAllAccesos, basename='accesos')
router.register(r'metodo-acceso', views.GetAllMetodo_Acceso, basename='metodo-acceso')

urlpatterns=[
    
    path('', include(router.urls)),

]