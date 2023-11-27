from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from propietarios import views

router = DefaultRouter()
router.register(r'propietarios', views.GetAllOwners,basename='propietarios')

urlpatterns=[
    
    path('', include(router.urls)),

]