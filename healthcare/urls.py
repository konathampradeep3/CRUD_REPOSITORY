from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorViewSet,
)

router = DefaultRouter()

router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'mappings', PatientDoctorViewSet, basename='mappings')

urlpatterns = [
    path('', include(router.urls)),
]