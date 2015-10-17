from django.db import models
from django.utils.translation import ugettext_lazy as _


class GenericKind(models.Model):
    kind = models.CharField(_('kind'), max_length=255)

    def __str__(self):
        return self.kind

    class Meta:
        abstract = True


class DirectedRelationKind(models.Model):
    kind = models.CharField(_('kind'), max_length=255)
    back = models.CharField(_('back'), max_length=255)

    def __str__(self):
        return '{} => {}'.format(self.kind, self.back)

    @property
    def reverse_relation(self):
        return '{} <= {}'.format(self.kind, self.back)

    class Meta:
        abstract = True
