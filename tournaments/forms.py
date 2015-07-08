from django import forms
from tournaments.models import Team
from django.utils.translation import ugettext_lazy as _

EMPTY_TEAM_ERROR = "Please enter a name for your team"

class TeamForm(forms.models.ModelForm):
    class Meta:
        model = Team
        fields = ('name',)
        widgets = {
            'name': forms.fields.TextInput(attrs={
                
            }),

        }
        error_messages = {
            'name': {'required': EMPTY_TEAM_ERROR}
        }