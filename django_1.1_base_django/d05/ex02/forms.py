from django import forms

class Ex02Form(forms.Form):
	text_input = forms.CharField(max_length=42)