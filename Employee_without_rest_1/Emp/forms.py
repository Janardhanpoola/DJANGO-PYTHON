from django import forms

from Emp.models import Emp

class Empform(forms.ModelForm):

    def clean_esal(self): #function for form validation
        inputsal=self.cleaned_data['esal']
        if inputsal<1000:
            raise forms.ValidationError("min sal is 1000")
        return inputsal


    class Meta:
        model=Emp  #model name created in models.py
        fields='__all__'
        