from django.db import models

# Create your models here.







# CONTACT MODEL
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName  = models.CharField(max_length=255)

    def __str__(self):
        return self.DepartmentName








# CONTACT MODEL
class Employees(models.Model):
    EmployeeId 	   = models.AutoField(primary_key=True)
    EmployeeName   = models.CharField(max_length=255)
    Department     = models.CharField(max_length=255)
    DateOfJoining  = models.DateField()
    photoFileName  = models.CharField(max_length=255)

    def __str__(self):
        return self.EmployeeName

