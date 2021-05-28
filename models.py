from django.db import models

# Create your models here.
class LSH(models.Model):
	Name		= models.CharField(label=max_length=120)
	Email 		= models.EmailField(blank=True, null=True)
	Message		= models.CharField(decimal_places=2, max_digits=10)
	Date		= models.DateField(null=True)



	


