from django.contrib import admin

from . import models


@admin.register(models.PersonEntityRelation)
class PersonEntityRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonEntityRelationKind)
class PersonEntityRelationKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonOrganizationRelation)
class PersonOrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonOrganizationRelationKind)
class PersonOrganizationKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityOrganizationRelation)
class EntityOrganizationRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityOrganizationRelationKind)
class EntityOrganizationRelationKindAdmin(admin.ModelAdmin):
    pass
