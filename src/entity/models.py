from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind, GenericKind


class EntityKind(GenericKind):

    class Meta:
        verbose_name = _('Entity Kind')


class Entity(models.Model):
    public_name = models.CharField(_('public name'), max_length=255)

    official_name = models.CharField(_('official name'), max_length=255, blank=True)
    official_id = models.CharField(_('official id'), max_length=255, blank=True)

    kind = models.ForeignKey(_('kind'), EntityKind, null=True, blank=True)

    description = models.TextField(_('description'), blank=True)

    image = models.ImageField(_('image'), blank=True)

    build = models.DateField(_('build'), blank=True, null=True)
    cease = models.DateField(_('cease'), blank=True, null=True)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    entity_relation = models.ManyToManyField(
        _('entity relation'),
        'self',
        symmetrical=False,
        through='EntityRelation',
        related_name='entity_relations')

    entity_organization_relation = models.ManyToManyField(
        _('entity organization relation'),
        'entity.Entity',
        through='cross_relations.EntityOrganizationRelation',
        related_name='entity_organization_relations')

    class Meta:
        verbose_name = _('Entity')

    def __str__(self):
        return self.public_name if self.public_name != '' else self.official_name


class EntityRelationKind(DirectedRelationKind):

    class Meta:
        verbose_name = _('Entity Relation Kind')


class EntityRelation(models.Model):
    entity = models.ForeignKey(_('entity'), Entity, related_name='entity_entity')
    relation = models.ForeignKey(_('relation'), Entity, related_name='entity_related_entity')
    kind = models.ForeignKey(_('kind'), EntityRelationKind)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    class Meta:
        verbose_name = _('Entity Relation')

    def __str__(self):
        return '{} : {} : {}'.format(self.entity, self.kind, self.relation)
