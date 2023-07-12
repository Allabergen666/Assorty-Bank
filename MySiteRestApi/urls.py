from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from restapi.views import (AnimeViewSet, CategoryViewSet, ContactSliderViewSet,
                           ContactViewSet, HomeImageViewSet,
                           HomeRowTextViewSet, PostViewSet, ProfileViewSet)

# Создаем объект OpenAPI для генерации спецификации Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API Documentation",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ],
)

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'anime', AnimeViewSet)
router.register(r'anime', AnimeViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'contactslider', ContactSliderViewSet)
router.register(r'homeimage', HomeImageViewSet)
router.register(r'hometext', HomeRowTextViewSet)
router.register(r'hometext', HomeRowTextViewSet)
router.register(r'post', PostViewSet)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
    path('graphql/', include('grapheneapi.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('redoc/', include('django.contrib.admindocs.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)