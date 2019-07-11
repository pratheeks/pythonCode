from django.db import models

# Create your models here.
class employee(models.Model):

	eno = models.IntegerField()
	ename = models.CharField(max_length=20)
	eaddr = models.CharField(max_length=50)


	def __str__(self):
		return '%s' %self.ename
    