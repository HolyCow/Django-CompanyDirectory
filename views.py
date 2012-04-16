from django.shortcuts import render_to_response
from companydirectory.models import Employee, Setting

def index(request):
   employees = Employee.objects.order_by('surname').all()
   sitename = Setting.objects.get(name__name__exact='Site Name').setting
   return render_to_response('companydirectory/template/companydirectory/index.html', {'employees': employees, 'sitename': sitename})
   
