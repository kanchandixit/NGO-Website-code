# main/forms.py

from django import forms
from .models import Campaign, ContactSubmission

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description', 'goal_amount', 'start_date', 'end_date']

class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'contact_method', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject of Your Message', 'class': 'form-control'}),
            'contact_method': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 5}),
        }

class DonationForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2) 