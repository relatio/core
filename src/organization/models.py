from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_hstore import hstore

from generics.abstract_models import DirectedRelationKind, GenericKind


class OrganizationKind(GenericKind):

    class Meta:
        verbose_name = _('Organization Kind')


class Organization(models.Model):

    public_name = models.CharField(_('public name'), max_length=255)

    description = models.TextField(_('description'), blank=True)

    kind = models.ForeignKey(OrganizationKind, null=True, blank=True, verbose_name=_('kind'))

    image = models.ImageField(_('image'), blank=True)

    build = models.DateField(_('build'), blank=True, null=True)
    cease = models.DateField(_('cease'), blank=True, null=True)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    organizational_relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='OrganizationalRelation',
        verbose_name=_('organization relation'),
        related_name='organizational_relations')

    class Meta:
        verbose_name = _('Organization')

    def __str__(self):
        return self.public_name


class OrganizationalRelationKind(DirectedRelationKind):

    class Meta:
        verbose_name = _('Organization Relation Kind')


class OrganizationalRelation(models.Model):
    organization = models.ForeignKey(Organization,
                                     verbose_name=_('organization'), related_name='organization_organization')
    relation = models.ForeignKey(Organization,
                                 verbose_name=_('relation'), related_name='organization_related_organization')
    kind = models.ForeignKey(OrganizationalRelationKind, verbose_name=_('kind'))

    metadata = hstore.DictionaryField(blank=True)

    class Meta:
        verbose_name = _('Organization Kind')

    def __str__(self):
        return '{} : {} : {}'.format(self.organization, self.kind, self.relation)
