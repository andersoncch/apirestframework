from rest_framework import viewsets
from rest_framework.response import Response
from django.db import connection
from .models import Departamento  # Asegúrate de que este modelo esté definido

class DepartamentoViewSet(viewsets.ViewSet):
    
     # Listar departamentos
    def list(self, request):
        query = "CALL ObtenerDepartamentos()"
        with connection.cursor() as cursor:
            cursor.execute(query)
            departamentos = cursor.fetchall()  # Obtener los resultados

        data = []
        for departamento in departamentos:
            data.append({
                "id": departamento[0],
                "nombre": departamento[1],
                "descripcion": departamento[2]
            })

        response = {
            "success": True,
            "message": "",
            "code_error": 0,
            "data": data,
            "query": query  # Mostrar el query que se ejecutó
        }

        return Response(response)

     # Crear un nuevo departamento
    def create(self, request):
        nombre = request.data.get('nombre')
        descripcion = request.data.get('descripcion')

        query = f"CALL InsertarDepartamento('{nombre}', '{descripcion}')"
        with connection.cursor() as cursor:
            cursor.execute(query)

        response = {
            "message": "Departamento creado exitosamente",
            "query": query  # Mostrar el query que se ejecutó
        }

        return Response(response, status=201)
    
    #Obtener un departamento por ID
    def retrieve(self, request, pk=None):
        query = f"CALL ObtenerDepartamentoPorID({pk})"
        with connection.cursor() as cursor:
            cursor.callproc('ObtenerDepartamentoPorID', [pk])
            departamento = cursor.fetchone()
            if departamento:
                response_data = {
                    'id': departamento[0],
                    'nombre': departamento[1],
                    'descripcion': departamento[2]
                }
                response = {
                    "success": True,
                    "message": "",
                    "code_error": 0,
                    "data": response_data,
                    "query": query  
                }
                return Response(response)

        return Response({"error": "Departamento no encontrado", "query": query}, status=404) 

     # Actualizar un departamento existente
    def update(self, request, pk=None):
        nombre = request.data.get('nombre')
        descripcion = request.data.get('descripcion')

        query = f"CALL ActualizarDepartamento({pk}, '{nombre}', '{descripcion}')"
        with connection.cursor() as cursor:
            cursor.execute(query)

        response = {
            "message": "Departamento actualizado exitosamente",
            "query": query  # Mostrar el query que se ejecutó
        }

        return Response(response, status=200)

    # Eliminar un departamento
    def destroy(self, request, pk=None):
        query = f"CALL EliminarDepartamento({pk})"
        with connection.cursor() as cursor:
            cursor.execute(query)

        response = {
            "message": "Departamento eliminado exitosamente",
            "query": query  # Mostrar el query que se ejecutó
        }

        return Response(response, status=204)