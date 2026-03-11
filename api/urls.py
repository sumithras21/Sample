from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, run_task
from django.urls import path, include

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('run-task/', run_task, name='run_task'),
]
