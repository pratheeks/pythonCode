from django import forms 
from databaseApp.models import student

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('sno','sname','sage')
    