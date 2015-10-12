from django import forms
from . import fields


class OrganizationRelationModelForm(forms.ModelForm):
    organization = fields.OrganizationSelect2Field()
    relation = fields.OrganizationSelect2Field()
    kind = fields.OrganizationalRelationKindSelect2Field()
