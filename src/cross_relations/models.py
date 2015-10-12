from django.db import models
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind
from person.models import Person
from entity.models import Entity
from organization.models import Organization


class PersonEntityRelationKind(DirectedRelationKind):
    pass


class PersonEntityRelation(models.Model):
    person = models.ForeignKey(Person, related_name='person_entity_person')
    entity = models.ForeignKey(Entity, related_name='person_entity_entity')
    kind = models.ForeignKey(PersonEntityRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    def __str__(self):
        return '{} : {} : {}'.format(self.person, self.kind, self.entity)


class PersonOrganizationRelationKind(DirectedRelationKind):
    pass


class PersonOrganizationRelation(models.Model):
    person = models.ForeignKey(Person, related_name='person_organization_person')
    organization = models.ForeignKey(Organization, related_name='person_organization_organization')
    kind = models.ForeignKey(PersonOrganizationRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    def __str__(self):
        return '{} : {} : {}'.format(self.person, self.kind, self.organization)


class EntityOrganizationRelationKind(DirectedRelationKind):
    pass


class EntityOrganizationRelation(models.Model):
    entity = models.ForeignKey(Entity, related_name='entity_organization_entity')
    organization = models.ForeignKey(Organization, related_name='entity_organization_organization')
    kind = models.ForeignKey(EntityOrganizationRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    def __str__(self):
        return '{} : {} : {}'.format(self.entity, self.kind, self.organization)
