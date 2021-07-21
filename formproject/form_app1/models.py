from django.db import models

# Create your models here.



class stud_reg(models.Model):
    name = models.CharField(max_length = 20)
    s_id = models.IntegerField()
    email = models.EmailField(max_length = 20)
    pas = models.CharField(max_length = 20)
