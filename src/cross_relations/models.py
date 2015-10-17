from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind
from person.models import Person
from entity.models import Entity
from organization.models import Organization


class PersonEntityRelationKind(DirectedRelationKind):
    pass


class PersonEntityRelation(models.Model):
    person = models.ForeignKey(_('person'), Person, related_name='person_entity_person')
    entity = models.ForeignKey(_('entity'), Entity, related_name='person_entity_entity')
    kind = models.ForeignKey(_('kind'), PersonEntityRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    class Meta:
        verbose_name = _('Person Entity Relation')

    def __str__(self):
        return '{} : {} : {}'.format(self.person, self.kind, self.entity)


class PersonOrganizationRelationKind(DirectedRelationKind):
    pass


class PersonOrganizationRelation(models.Model):
    person = models.ForeignKey(_('person'), Person, related_name='person_organization_person')
    organization = models.ForeignKey(_('organization'), Organization, related_name='person_organization_organization')
    kind = models.ForeignKey(_('kind'), PersonOrganizationRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    def __str__(self):
        return '{} : {} : {}'.format(self.person, self.kind, self.organization)

    class Meta:
        verbose_name = _('Person Organization Relation')


class EntityOrganizationRelationKind(DirectedRelationKind):
    pass


class EntityOrganizationRelation(models.Model):
    entity = models.ForeignKey(_('entity'), Entity, related_name='entity_organization_entity')
    organization = models.ForeignKey(_('organization'), Organization, related_name='entity_organization_organization')
    kind = models.ForeignKey(_('kind'), EntityOrganizationRelationKind)

    metadata = hstore.DictionaryField(blank=True)

    class Meta:
        verbose_name = _('Entity Organization Relation')

    def __str__(self):
        return '{} : {} : {}'.format(self.entity, self.kind, self.organization)
