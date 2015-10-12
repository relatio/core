from django.contrib import admin

from . import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationKind)
class OrganizationKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationalRelation)
class OrganizationalRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationalRelationKind)
class OrganizationalRelationKindAdmin(admin.ModelAdmin):
    pass
