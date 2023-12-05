from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from operadoras import views

router = DefaultRouter()
router.register(r'operadoras', views.GetAllOperadora, basename='operadoras')


urlpatterns=[
    
    path('', include(router.urls)),

]