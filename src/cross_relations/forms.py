from django import forms

from person.fields import PersonSelect2Field
from entity.fields import EntitySelect2Field
from organization.fields import OrganizationSelect2Field

from . import fields


class PersonEntityRelationModelForm(forms.ModelForm):
    person = PersonSelect2Field()
    entity = EntitySelect2Field()
    kind = fields.PersonEntityRelationKindSelect2Field()


class PersonOrganizationRelationModelForm(forms.ModelForm):
    person = PersonSelect2Field()
    organization = OrganizationSelect2Field()
    kind = fields.PersonOrganizationRelationKindSelect2Field()


class EntityOrganizationRelationModelForm(forms.ModelForm):
    entity = EntitySelect2Field()
    organization = OrganizationSelect2Field()
    kind = fields.EntityOrganizationRelationKindSelect2Field()
