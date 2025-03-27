from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

	class Meta:
		model = User
		fields = ["username", "password"]

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		password_confirmation = cleaned_data.get("password_confirmation")
		if password != password_confirmation:
			raise forms.ValidationError("Passwords do not match.")
		return cleaned_data
