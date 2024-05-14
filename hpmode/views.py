from django.http import JsonResponse
from django.shortcuts import render


from hpmode.models import Employee
from hpmode.serializers import EmployeeSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializers(employee, many=True)
        return JsonResponse({'employee': serializer.data})
    if request.method == 'POST':
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

