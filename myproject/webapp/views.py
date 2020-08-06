from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeesSerializer

# Create your views here.

class employeeList(APIView):

    def get(self,request):
        all_employees = employees.objects.all()
        serializer = employeesSerializer(all_employees,many=True) 
        return Response(serializer.data)


    def post(self,request):
        pass
    

