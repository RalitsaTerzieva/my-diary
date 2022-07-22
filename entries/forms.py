from django import forms

class EntryForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)