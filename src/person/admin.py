# from django.utils.safestring import mark_safe
from django.contrib import admin

from import_export.admin import ImportExportMixin

from . import models, forms, fields


@admin.register(models.Person)
class PersonAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = fields.PersonImportExportResource

    # readonly_fields = ('image_preview',)
    #
    # def image_preview(self, obj):
    #     if obj.image:
    #         url = obj.image.url
    #         return mark_safe("<img id='image' src='%s' style='max-width:150px;max-height:150px;' />" % url)
    #     else:
    #         return ""
    # image_preview.short_description = "Preview"


@admin.register(models.PersonalRelation)
class PersonalRelationAdmin(admin.ModelAdmin):
    fields = (('person', 'kind', 'relation'),)
    form = forms.PersonalRelationModelForm


@admin.register(models.PersonalRelationKind)
class PersonalRelationKindAdmin(admin.ModelAdmin):
    pass
