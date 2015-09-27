from django.db import models

# Create your models here.

class Organization(models.Model):
    # kind = 

    public_name = models.CharField(max_length=255)
    
    description = models.TextField(blank=True)

    image = models.ImageField(blank=True)

    build = models.DateField(blank=True, null=True)
    cease = models.DateField(blank=True, null=True)

    # direction
    # locality
    # country
    # telephone
    # email
    
    def __src__(self):
        return self.public_name
