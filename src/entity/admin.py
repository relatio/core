from django.contrib import admin

from . import models, forms


@admin.register(models.Entity)
class EntityAdmin(admin.ModelAdmin):
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
