from rest_framework import serializers
from .models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'  # O especifica los campos que quieras incluir
