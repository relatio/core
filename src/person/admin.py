from django.contrib import admin

from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonalRelation)
class PersonalRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonalRelationKind)
class PersonalRelationKindAdmin(admin.ModelAdmin):
    pass
