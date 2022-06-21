from django.urls import path
from .views import *


urlpatterns = [
	path('department/', departmentApi),
	path('department/<int:id>/', departmentApi),

	path('employee/', employeeApi),
	path('employee/<int:id>/', employeeApi),

	path('Employee/SaveFile/', saveFile),
]