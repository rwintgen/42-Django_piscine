from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput, label="Password")
	password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

	class Meta:
		model = User
		fields = ['username']

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		password_confirm = cleaned_data.get("password_confirm")

		if password != password_confirm:
			raise forms.ValidationError("Passwords do not match.")
		return cleaned_data
	
class LogInForm(forms.Form):
	username = forms.CharField(max_length=150, label="Username")
	password = forms.CharField(widget=forms.PasswordInput, label="Password")
