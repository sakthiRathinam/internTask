from django.db import models

# Create your models here.
from django.db import models

class user(models.Model):
	IDD=models.CharField(max_length=200,null=False)
	name= models.CharField(max_length=200,null=True)
	timezone=models.CharField(max_length=200,null=True)
	date=models.DateTimeField(null=True,blank=True)
	def __str__(self):
		return self.name
class Activity(models.Model):
	start_time=models.DateTimeField(blank=True,null=True)
	end_time=models.DateTimeField(blank=True,null=True)
	user=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
