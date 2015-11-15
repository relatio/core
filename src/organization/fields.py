from django_select2.fields import AutoModelSelect2Field
from import_export.resources import ModelResource

from .models import Organization, OrganizationalRelationKind


class OrganizationSelect2Field(AutoModelSelect2Field):
    queryset = Organization.objects
    search_fields = ['public_name__icontains']


class OrganizationalRelationKindSelect2Field(AutoModelSelect2Field):
    queryset = OrganizationalRelationKind.objects
    search_fields = ['kind__icontains', 'back__icontains']


class OrganizationImportExportResource(ModelResource):
    class Meta:
        model = Organization
