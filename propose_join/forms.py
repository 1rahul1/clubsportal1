from django import forms
from .models import ProposedClub

class club_logo(forms.ModelForm):
    class Meta:
        model = ProposedClub
        fields = ('club_name','club_info','club_logo')