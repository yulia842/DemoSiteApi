from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, CartViewSet

router = routers.DefaultRouter()
router.register("products",ProductViewSet)
router.register("carts",CartViewSet)
urlpatterns = [
    path('',include(router.urls))
]
