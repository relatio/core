from django.contrib import admin
from import_export.admin import ImportExportMixin

from . import models, forms, fields


@admin.register(models.Entity)
class EntityAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = fields.EntityImportExportResource
    pass


@admin.register(models.EntityKind)
class EntityKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityRelation)
class EntityRelationAdmin(admin.ModelAdmin):
    fields = (('entity', 'kind', 'relation'),)
    form = forms.EntityRelationModelForm


@admin.register(models.EntityRelationKind)
class EntityRelationKindAdmin(admin.ModelAdmin):
    pass
