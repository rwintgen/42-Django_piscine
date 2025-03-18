from django import forms

class Ex02Form(forms.Form):
	input = forms.CharField(max_length=42)