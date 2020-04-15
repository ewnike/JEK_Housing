from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Contact

#class ContactUsForm(forms.Form):
    #first_name = forms.CharField(max_length=45)
    #last_name = forms.CharField(max_length=45)
    #email = forms.EmailField()
    #message = forms.CharField(widget=forms.Textarea)


class ContactUsForm(forms.ModelForm):
  class Meta:
      model = Contact
      fields = '__all__'
