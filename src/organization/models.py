from django.db import models
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind, GenericKind


class OrganizationKind(GenericKind):
    pass


class Organization(models.Model):

    public_name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    image = models.ImageField(blank=True)

    build = models.DateField(blank=True, null=True)
    cease = models.DateField(blank=True, null=True)

    metadata = hstore.DictionaryField(blank=True)

    organizational_relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='OrganizationalRelation',
        related_name='organizational_relations')

    def __src__(self):
        return self.public_name


class OrganizationalRelationKind(DirectedRelationKind):
    pass


class OrganizationalRelation(models.Model):
    organization = models.ForeignKey(Organization, related_name='organization_organization')
    relation = models.ForeignKey(Organization, related_name='organization_related_organization')
    kind = models.ForeignKey(OrganizationalRelationKind)

    metadata = hstore.DictionaryField(blank=True)
