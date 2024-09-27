from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend  # Importar DjangoFilterBackend
from .models import Company, Employee
from .serializer import CompanySerializer, EmployeeSerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend,)  # Cambia a DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  # Define el conjunto de consultas para Employee
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)  # Cambia a DjangoFilterBackend
    filterset_fields = ['company']  # Permitir filtrado por ID de compañía