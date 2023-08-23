from django.urls import path, include
from rest_framework import routers
from .views import SkillViewSet, ProjectViewSet, ProjectRatingViewSet, EducationViewSet

router = routers.DefaultRouter()
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
router.register('projectrating', ProjectRatingViewSet)
router.register('education', EducationViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
