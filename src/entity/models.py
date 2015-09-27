from django.db import models

# Create your models here.


class Entity(models.Model):
    # kind = 

    public_name = models.CharField(max_length=255)
    
    official_name = models.CharField(max_length=255, blank=True)
    official_id = models.CharField(max_length=255, blank=True)

    description = models.TextField(blank=True)

    image = models.ImageField()

    build = models.DateField(blank=True, null=True)
    cease = models.DateField(blank=True, null=True)

    # direction
    # locality
    # country
    # telephone
    # email
    
    def __src__(self):
        return self.offcial_name if self.offcial_name != '' else self.public_name
