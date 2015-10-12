from django.db import models


class GenericKind(models.Model):
    kind = models.CharField(max_length=255)

    def __str__(self):
        return self.kind

    class Meta:
        abstract = True


class DirectedRelationKind(models.Model):
    kind = models.CharField(max_length=255)
    back = models.CharField(max_length=255)

    def __str__(self):
        return '{} => {}'.format(self.kind, self.back)

    @property
    def reverse_relation(self):
        return '{} <= {}'.format(self.kind, self.back)

    class Meta:
        abstract = True
