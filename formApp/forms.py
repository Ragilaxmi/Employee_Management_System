from django import forms
from django.core.exceptions import ValidationError
from DBApp.models import Employee
class FirstForm(forms.Form):
    value1=forms.IntegerField()
    value2=forms.IntegerField()
    def clean_value1(self):
        v1=self.cleaned_data['value1']
        if v1<0:
           raise ValidationError('Nagitive Error are not allowed')
        return v1
    def clean_value2(self):
        v2=self.changed_data['value2']

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        

