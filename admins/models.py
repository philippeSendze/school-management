from django.db import models


class BaseAdmin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    
    class Meta:
        abstract = True
    
class Director(BaseAdmin):
    date_of_taking_office = models.DateField()
    active = models.BooleanField(default=False)
    
    class Meta:
        db_table = "director"
        

class Administrator(BaseAdmin):
    
    class Meta:
        db_table = "administrator"
        

class Secretary(BaseAdmin):
    
    class Meta:
        db_table = "secretary"
        

class Accountant(BaseAdmin):
    
    class Meta:
        db_table = "accountant"