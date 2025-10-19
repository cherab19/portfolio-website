# core/forms.py
from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }
    
    # Simple honeypot field for spam protection
    honeypot = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'd-none'}))
    
    def clean_honeypot(self):
        honeypot = self.cleaned_data.get('honeypot')
        if honeypot:
            raise forms.ValidationError("Spam detected.")
        return honeypot