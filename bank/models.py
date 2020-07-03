from django.db import models

# Create your models here.
class banks(models.Model):
	name = models.CharField(max_length=49)
	id_b = models.BigIntegerField(null=False)
class branchesd(models.Model):
	ifsc = models.CharField(max_length=11,null=False)
	bank_id = models.BigIntegerField()
	branch = models.CharField(max_length=74)
	address = models.CharField(max_length=195)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=26)
