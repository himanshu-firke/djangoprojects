from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 6, "cols": 60}), label="Enter Text")
