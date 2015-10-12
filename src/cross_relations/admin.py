from django.contrib import admin

from . import models, forms


@admin.register(models.PersonEntityRelation)
class PersonEntityRelationAdmin(admin.ModelAdmin):
    fields = (('person', 'kind', 'entity'),)
    form = forms.PersonEntityRelationModelForm


@admin.register(models.PersonEntityRelationKind)
class PersonEntityRelationKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonOrganizationRelation)
class PersonOrganizationAdmin(admin.ModelAdmin):
    fields = (('person', 'kind', 'organization'),)
    form = forms.PersonOrganizationRelationModelForm


@admin.register(models.PersonOrganizationRelationKind)
class PersonOrganizationKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityOrganizationRelation)
class EntityOrganizationRelationAdmin(admin.ModelAdmin):
    fields = (('entity', 'kind', 'organization'),)
    form = forms.EntityOrganizationRelationModelForm


@admin.register(models.EntityOrganizationRelationKind)
class EntityOrganizationRelationKindAdmin(admin.ModelAdmin):
    pass
