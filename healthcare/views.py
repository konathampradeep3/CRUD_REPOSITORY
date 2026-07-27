from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Patient, Doctor, PatientDoctor
from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    PatientDoctorSerializer
)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class PatientDoctorViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.request.query_params.get("patient_id")

        if patient_id:
            return PatientDoctor.objects.filter(patient_id=patient_id)

        return PatientDoctor.objects.all()
