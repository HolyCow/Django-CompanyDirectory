from django.shortcuts import render_to_response
from companydirectory.models import Employee

def index(request):
   employees = Employee.objects.all()
   return render_to_response('companydirectory/template/companydirectory/index.html', {'employees': employees})
   
