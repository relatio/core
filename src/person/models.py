from django.db import models
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    public_name = models.CharField(max_length=510, blank=True)

    position = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    image = models.ImageField(blank=True)

    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)

    metadata = hstore.DictionaryField(blank=True)

    personal_relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='PersonalRelation',
        related_name='personal_relations')

    person_entity_relation = models.ManyToManyField(
        'entity.Entity',
        through='cross_relations.PersonEntityRelation',
        related_name='person_entity_relations')

    person_organization_relation = models.ManyToManyField(
        'organization.Organization',
        through='cross_relations.PersonOrganizationRelation',
        related_name='person_organization_relations')

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def alias(self):
        return self.public_name if self.public_name != '' else self.get_full_name()

    def __str__(self):
        return self.alias


class PersonalRelationKind(DirectedRelationKind):
    pass


class PersonalRelation(models.Model):
    person = models.ForeignKey(Person, related_name='person_person')
    relation = models.ForeignKey(Person, related_name='peson_related_person')
    kind = models.ForeignKey(PersonalRelationKind)

    metadata = hstore.DictionaryField(blank=True)
