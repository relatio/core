from django import forms
from . import fields


class EntityRelationModelForm(forms.ModelForm):
    entity = fields.EntitySelect2Field()
    relation = fields.EntitySelect2Field()
    kind = fields.EntityRelationKindSelect2Field()
