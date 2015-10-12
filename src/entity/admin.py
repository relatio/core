from django.contrib import admin

from . import models


@admin.register(models.Entity)
class EntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityKind)
class EntityKindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityRelation)
class EntityRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EntityRelationKind)
class EntityRelationKindAdmin(admin.ModelAdmin):
    pass
