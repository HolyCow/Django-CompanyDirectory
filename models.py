from django.db import models
from datetime import datetime

# Create your models here.
      
class Department(models.Model):
   name = models.CharField(max_length=100)
   def __unicode__(self):
      return self.name
   
class Location(models.Model):
   name = models.CharField(max_length=100)
   def __unicode__(self):
      return self.name
   
class Shift(models.Model):
   name = models.CharField(max_length=20)
   def __unicode__(self):
      return self.name
   
class Employee(models.Model):
   firstname = models.CharField(max_length=30)
   surname = models.CharField(max_length=50)
   title = models.CharField(max_length=100)
   department = models.ForeignKey(Department)
   location = models.ForeignKey(Location)
   extension = models.CharField(max_length=10)
   shift = models.ForeignKey(Shift)
   email = models.EmailField(max_length=100)
   supervisor = models.ForeignKey("self", blank=True, null=True)
   create_date = models.DateField(default=datetime.now, editable=False)
   modified_date = models.DateField(default=datetime.now, editable=False)
   def __unicode__(self):
      return self.firstname + ' ' + self.surname
   def save(self, *args, **kwargs):
        self.modified = datetime.today()
        super(Employee, self).save(*args, **kwargs)



