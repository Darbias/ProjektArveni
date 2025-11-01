from django import forms
from .models import ContactMessage, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name","email","phone","subject","message"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Emri"}),
            "email": forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email"}),
            "phone": forms.TextInput(attrs={"class":"form-control", "placeholder":"Tel (opsionale)"}),
            "subject": forms.TextInput(attrs={"class":"form-control", "placeholder":"Subjekti"}),
            "message": forms.Textarea(attrs={"class":"form-control", "rows":5, "placeholder":"Mesazhi"}),
        }

class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["name","email","phone","service","message"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Emri"}),
            "email": forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email"}),
            "phone": forms.TextInput(attrs={"class":"form-control", "placeholder":"Tel (opsionale)"}),
            "service": forms.Select(attrs={"class":"form-select"}),
            "message": forms.Textarea(attrs={"class":"form-control", "rows":4, "placeholder":"Përshkruaj nevojat"}),
        }
