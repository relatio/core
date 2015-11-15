from django_select2.fields import AutoModelSelect2Field
from import_export.resources import ModelResource

from .models import Person, PersonalRelationKind


class PersonSelect2Field(AutoModelSelect2Field):
    queryset = Person.objects
    search_fields = ['public_name__icontains', 'first_name__icontains', 'last_name__icontains']


class PersonalRelationKindSelect2Field(AutoModelSelect2Field):
    queryset = PersonalRelationKind.objects
    search_fields = ['kind__icontains', 'back__icontains']


class PersonImportExportResource(ModelResource):
    class Meta:
        model = Person
