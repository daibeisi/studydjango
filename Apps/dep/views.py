from rest_framework import generics
from rest_framework import permissions
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
