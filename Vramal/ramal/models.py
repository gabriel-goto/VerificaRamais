from django.db import models

class Ramal(models.Model):

	Ramal_id = models.AutoField(primary_key=True)
	Ramal_Number = models.CharField(max_length=5)


	def __str__(self):
		return self.Ramal_Number
		

class pessoa(models.Model):
	
	pessoa_nome = models.CharField(max_length=10)

	def __str__(self):
		return self.pessoa_nome