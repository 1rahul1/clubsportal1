from django import forms
from .models import ProposedClub,ExistingClub

class club_logo(forms.ModelForm):
    class Meta:
        model = ProposedClub
        fields = ('club_name','club_info','club_logo')


# class club_join(forms.ModelForm):
#     class Meta:
#         model = ClubMember
#         fields=('clubs_joined',)