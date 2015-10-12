from django.db import models
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind, GenericKind


class EntityKind(GenericKind):
    pass


class Entity(models.Model):
    public_name = models.CharField(max_length=255)

    official_name = models.CharField(max_length=255, blank=True)
    official_id = models.CharField(max_length=255, blank=True)

    kind = models.ForeignKey(EntityKind, null=True, blank=True)

    description = models.TextField(blank=True)

    image = models.ImageField(blank=True)

    build = models.DateField(blank=True, null=True)
    cease = models.DateField(blank=True, null=True)

    metadata = hstore.DictionaryField(blank=True)

    entity_relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='EntityRelation',
        related_name='entity_relations')

    entity_organization_relation = models.ManyToManyField(
        'entity.Entity',
        through='cross_relations.EntityOrganizationRelation',
        related_name='entity_organization_relations')

    def __str__(self):
        return self.public_name if self.public_name != '' else self.official_name


class EntityRelationKind(DirectedRelationKind):
    pass


class EntityRelation(models.Model):
    entity = models.ForeignKey(Entity, related_name='entity_entity')
    relation = models.ForeignKey(Entity, related_name='entity_related_entity')
    kind = models.ForeignKey(EntityRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    def __str__(self):
        return '{} : {} : {}'.format(self.entity, self.kind, self.relation)
