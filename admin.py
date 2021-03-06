from companydirectory.models import Employee, Shift, Department, Location, Setting
from django.contrib import admin

#   title = models.CharField(max_length=100)
#   department = models.ForeignKey(Department)
#   location = models.ForeignKey(Location)
#   extension = models.CharField(max_length=10)
#   shift = models.ForeignKey(Shift)
#   email = models.CharField(max_length=100)
#   supervisor = models.ManyToManyField("self", blank=True, null=True, symmetrical=False)
#   create_date = models.DateField(default=datetime.now, editable=False)
#   modified_date = models.DateField(default=datetime.now, editable=False)
   
class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('__unicode__', 'email', 'title', 'department', 'supervisor', 'create_date', 'modified_date')
   list_filter = ['department']
   def formfield_for_foreignkey(self, db_field, request, **kwargs):
      if db_field.name == "supervisor":
         kwargs["queryset"] = Employee.objects.filter(is_supervisor=True)
      return super(EmployeeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class SettingAdmin(admin.ModelAdmin):
   list_display = ('name', '__unicode__')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Shift)
admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Setting, SettingAdmin)

