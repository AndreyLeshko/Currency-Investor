from django import forms

class New_Post(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)