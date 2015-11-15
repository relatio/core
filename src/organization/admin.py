from django.contrib import admin
from import_export.admin import ImportExportMixin

from . import models, forms, fields


@admin.register(models.Organization)
class OrganizationAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = fields.OrganizationImportExportResource
    pass


@admin.register(models.OrganizationKind)
class OrganizationKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationalRelation)
class OrganizationalRelationAdmin(admin.ModelAdmin):
    fields = (('organization', 'kind', 'relation'),)
    form = forms.OrganizationRelationModelForm


@admin.register(models.OrganizationalRelationKind)
class OrganizationalRelationKindAdmin(admin.ModelAdmin):
    pass
