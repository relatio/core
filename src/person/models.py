from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    public_name = models.CharField(max_length=510, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)
    # direction
    # locality
    # country
    # telephone
    # email

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def alias(self):
        
        return self.public_name if self.public_name != ''  else self.get_full_name()

    def __str__(self):
        return self.alias
