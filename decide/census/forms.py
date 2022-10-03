from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from voting.models import Voting

class CensusForm(forms.Form):

    t_ids1 = tuple((u.get('id'), "Id: "+str(u.get('id'))+" Nombre: "+str(u.get('first_name'))) for u in User.objects.values())
    t_ids2 = tuple((v.get('id'), str(v.get('name'))) for v in Voting.objects.all().filter(end_date__isnull=True).values())

    '''voting_id = forms.ChoiceField(label='Open votings', choices=t_ids2, required=True,
    widget=forms.Select(attrs={'style': 'width: 300px;','class': 'form-control'}))'''

    voting = forms.ModelChoiceField(label='Open votings', empty_label="-", queryset=Voting.objects.all().filter(end_date__isnull=True), required=True,
    widget=forms.Select(attrs={'style': 'width: 300px;','class': 'form-control'}))
    
    voters = forms.MultipleChoiceField(label='Open votings', choices=t_ids1, required=True,
    widget=forms.CheckboxSelectMultiple())
