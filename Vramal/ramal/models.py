from django.db import models

class Ramal(models.Model):

	Ramal_id = models.AutoField(primary_key=True)
	Ramal_Number = models.CharField(max_length=5)

class pessoa(models.Model):
	
	pessoa_nome = models.CharField(max_length=10)