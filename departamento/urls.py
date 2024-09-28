from django.urls import path
from .views import DepartamentoViewSet

urlpatterns = [
    path('departamento/list/', DepartamentoViewSet.as_view({'get': 'list'}), name='obtener_departamentos'),
    path('departamento/insertar/', DepartamentoViewSet.as_view({'post': 'create'}), name='insertar_departamento'),
    path('departamento/<int:pk>/', DepartamentoViewSet.as_view({'get': 'retrieve'}), name='obtener_departamento_por_id'),
    path('departamento/actualizar/<int:pk>/', DepartamentoViewSet.as_view({'put': 'update'}), name='actualizar_departamento'),
    path('departamento/eliminar/<int:pk>/', DepartamentoViewSet.as_view({'delete': 'destroy'}), name='eliminar_departamento'),
]

