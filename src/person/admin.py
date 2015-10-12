from django.contrib import admin

from . import models, forms


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonalRelation)
class PersonalRelationAdmin(admin.ModelAdmin):
    fields = (('person', 'kind', 'relation'),)
    form = forms.PersonalRelationModelForm


@admin.register(models.PersonalRelationKind)
class PersonalRelationKindAdmin(admin.ModelAdmin):
    pass
