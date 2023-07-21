from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
