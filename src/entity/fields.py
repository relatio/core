from django_select2.fields import AutoModelSelect2Field

from .models import Entity, EntityRelationKind


class EntitySelect2Field(AutoModelSelect2Field):
    queryset = Entity.objects
    search_fields = ['public_name__icontains', 'official_name__icontains', 'official_id__icontains']


class EntityRelationKindSelect2Field(AutoModelSelect2Field):
    queryset = EntityRelationKind.objects
    search_fields = ['kind__icontains', 'back__icontains']
