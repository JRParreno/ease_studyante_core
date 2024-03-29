"""
URL configuration for ease_studyante_core project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import path, include, re_path
from rest_framework import permissions
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from ease_studyante_core import settings
from ease_studyante_core.views import TokenViewWithUserId


schema_view = get_schema_view(
    openapi.Info(
        title="Smart libary hub API",
        default_version='v1',
        description="Testing API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'),),
    path('o/login/', TokenViewWithUserId.as_view(), name='token'),
]

urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
