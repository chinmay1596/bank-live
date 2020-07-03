from django.db import models

class Bank(models.Model):
	ifsc = models.CharField(max_length=500, unique=True)
	bank_id = models.IntegerField()
	branch_name = models.CharField(max_length=255)
	address = models.TextField()
	city = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	bank_name = models.CharField(max_length=400)

	def __str__(self):
		return "{}-{}".format(self.bank_name, self.branch_name)