from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Patient
from api_app.serializers import PatientSerializers

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    
# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializers
