from django_select2.fields import AutoModelSelect2Field

from .models import (
    PersonEntityRelationKind, PersonOrganizationRelationKind, EntityOrganizationRelationKind
)


class PersonEntityRelationKindSelect2Field(AutoModelSelect2Field):
    queryset = PersonEntityRelationKind.objects
    search_fields = ['kind__icontains', 'back__icontains']


class PersonOrganizationRelationKindSelect2Field(AutoModelSelect2Field):
    queryset = PersonOrganizationRelationKind.objects
    search_fields = ['kind__icontains', 'back__icontains']


class EntityOrganizationRelationKindSelect2Field(AutoModelSelect2Field):
    queryset = EntityOrganizationRelationKind.objects
    search_fields = ['kind__icontains', 'back__icontains']
