from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=255, required=True)
    content = forms.CharField(min_length=10, max_length=1024, widget=forms.Textarea, required=True)