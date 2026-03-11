from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course

class CourseAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        Course.objects.create(name="Sumithra", duration="4 years", fees=275000)

    def test_get_courses(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
