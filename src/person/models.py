from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind


class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)

    public_name = models.CharField(_('public name'), max_length=510, blank=True)

    position = models.CharField(_('position'), max_length=255, blank=True)

    description = models.TextField(_('description'), blank=True)

    image = models.ImageField(_('image'), blank=True)

    born = models.DateField(_('born'), blank=True, null=True)
    died = models.DateField(_('died'), blank=True, null=True)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    personal_relation = models.ManyToManyField(
        _('personal relation'),
        'self',
        symmetrical=False,
        through='PersonalRelation',
        related_name='personal_relations')

    person_entity_relation = models.ManyToManyField(
        _('personal entity relation'),
        'entity.Entity',
        through='cross_relations.PersonEntityRelation',
        related_name='person_entity_relations')

    person_organization_relation = models.ManyToManyField(
        _('personal organization relation'),
        'organization.Organization',
        through='cross_relations.PersonOrganizationRelation',
        related_name='person_organization_relations')

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def alias(self):
        return self.public_name if self.public_name != '' else self.get_full_name()

    class Meta:
        verbose_name = _('Person')

    def __str__(self):
        return self.alias


class PersonalRelationKind(DirectedRelationKind):

    class Meta:
        verbose_name = _('Person Relation Kind')


class PersonalRelation(models.Model):
    person = models.ForeignKey(_('person'), Person, related_name='person_person')
    relation = models.ForeignKey(_('relation'), Person, related_name='peson_related_person')
    kind = models.ForeignKey(_('kind'), PersonalRelationKind)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    class Meta:
        verbose_name = _('Person Relation')

    def __str__(self):
        return '{} : {} : {}'.format(self.person, self.kind, self.relation)
