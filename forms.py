from django import forms

class QuoteForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.EmailField(label='Email address', required=True)
    website = forms.URLField(label='Current website', required=False)
    number = forms.CharField(label='Contact number', required=True)
    about = forms.CharField(label='About the project', widget=forms.Textarea, required=True)


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    
      
