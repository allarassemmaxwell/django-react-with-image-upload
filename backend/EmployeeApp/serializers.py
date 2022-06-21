from rest_framework import serializers

from .models import *
from django.http import Http404




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Departments
        fields = [
            'DepartmentId',
            'DepartmentName',    
        ]




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Employees
        fields = [
            'EmployeeId',
            'EmployeeName', 
            'Department',
            'DateOfJoining',
            'photoFileName'   
        ]