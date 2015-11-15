from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_hstore import hstore
from phonenumber_field.modelfields import PhoneNumberField

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

    id_card_number = models.CharField(_('id card number'), blank=True, max_length=1000)
    social_security_number = models.CharField(_('social security number'), blank=True, max_length=1000)

    email_1 = models.EmailField(_('email 1'), blank=True)
    email_2 = models.EmailField(_('email 2'), blank=True)

    phone_1 = PhoneNumberField(_('phone 1'), blank=True)
    phone_2 = PhoneNumberField(_('phone 2'), blank=True)

    address = models.CharField(_('address'), blank=True, max_length=1000)

    facebook = models.CharField(_('facebook'), blank=True, max_length=1000)
    twitter = models.CharField(_('twitter'), blank=True, max_length=1000)
    instagram = models.CharField(_('instagram'), blank=True, max_length=1000)

    webpage = models.CharField(_('webpage'), blank=True, max_length=1000)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    personal_relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='PersonalRelation',
        verbose_name=_('personal relation'),
        related_name='personal_relations')

    person_entity_relation = models.ManyToManyField(
        'entity.Entity',
        through='cross_relations.PersonEntityRelation',
        verbose_name=_('personal entity relation'),
        related_name='person_entity_relations')

    person_organization_relation = models.ManyToManyField(
        'organization.Organization',
        through='cross_relations.PersonOrganizationRelation',
        verbose_name=_('personal organization relation'),
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
    person = models.ForeignKey(Person, verbose_name=_('person'), related_name='person_person')
    relation = models.ForeignKey(Person, verbose_name=_('relation'), related_name='peson_related_person')
    kind = models.ForeignKey(PersonalRelationKind, verbose_name=_('kind'))

    start = models.DateField(_('start'), blank=True, null=True)
    end = models.DateField(_('end'), blank=True, null=True)

    metadata = hstore.DictionaryField(_('metadata'), blank=True)

    class Meta:
        verbose_name = _('Person Relation')

    def __str__(self):
        return '{} : {} : {}'.format(self.person, self.kind, self.relation)
