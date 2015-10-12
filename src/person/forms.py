from django import forms

from . import fields


class PersonalRelationModelForm(forms.ModelForm):
    person = fields.PersonSelect2Field()
    relation = fields.PersonSelect2Field()
    kind = fields.PersonalRelationKindSelect2Field()
