"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Creación de ficha API",
        default_version='v1',
        description='Uso El backend proporciona una API REST ',
        contact=openapi.Contact(email="stalinvega18@gmail.com"),
        lilicense=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('api_ficha_crea/admin/', admin.site.urls),
    path('api_ficha_crea/',include('tipo_estacion.urls')),
    path('api_ficha_crea/',include('propietarios.urls')),
    path('api_ficha_crea/',include('ubicacion.urls')),
    path('api_ficha_crea/',include('accesos.urls')),
    path('api_ficha_crea/',include('tipo_observacion.urls')),
    path('api_ficha_crea/',include('tipo_estacion.urls')),
    path('api_ficha_crea/',include('estado_estaciones.urls')),
    path('api_ficha_crea/',include('puntos_observacion.urls')),
    path('api_ficha_crea/',include('estaciones.urls')),
    # Rutas para Swagger
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
