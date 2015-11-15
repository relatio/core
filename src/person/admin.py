from django.contrib import admin
from import_export.admin import ImportExportMixin

from . import models, forms, fields


@admin.register(models.Person)
class PersonAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = fields.PersonImportExportResource
    pass


@admin.register(models.PersonalRelation)
class PersonalRelationAdmin(admin.ModelAdmin):
    fields = (('person', 'kind', 'relation'),)
    form = forms.PersonalRelationModelForm


@admin.register(models.PersonalRelationKind)
class PersonalRelationKindAdmin(admin.ModelAdmin):
    pass
