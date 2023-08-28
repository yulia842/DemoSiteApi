from rest_framework import routers
from django.urls import path, include
from .views import ContactViewSet, JokesViewSet
router = routers.DefaultRouter()
router.register('contact', ContactViewSet)
router.register('joke', JokesViewSet)
urlpatterns = [
    path('', include(router.urls))
]
