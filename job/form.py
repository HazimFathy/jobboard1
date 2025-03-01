from django import forms
from .models import apply , Job


class applyform(forms.ModelForm):
    class Meta:
        model=apply
        fields=['name','email','website','cv','coverletter']
        
        
class addjob(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('owner','slug')
        