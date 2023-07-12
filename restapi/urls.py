from rest_framework import permissions, routers

from .views import (AnimeViewSet, CategoryViewSet, ContactSliderViewSet,
                    ContactViewSet, HomeImageViewSet, HomeRowTextViewSet,
                    PostViewSet, ProfileViewSet)

router = routers.DefaultRouter()

router.register('api/category', CategoryViewSet, basename='category')
router.register('api/profile', ProfileViewSet, basename='profile')
# router.register('api/user', UserSerializer, basename='user')
router.register('api/anime', AnimeViewSet, basename='anime')
router.register('api/contact', ContactViewSet, basename='contact')
router.register('api/contactslider', ContactSliderViewSet, basename='contactslider')
router.register('api/contactslider', ContactSliderViewSet, basename='contactslider')
router.register('api/homeimage', HomeImageViewSet, basename='homeimage')
router.register('api/homerowtext', HomeRowTextViewSet, basename='homerowtext')
router.register('api/post', PostViewSet, basename='post')

urlpatterns = router.urls