from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets
from .tasks import test_task
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@api_view(['GET'])
def run_task(request):

    test_task.delay()

    return Response({"message": "Task sent to background"})