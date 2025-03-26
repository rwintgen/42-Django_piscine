from django import forms
from .models import CustomUser, Tip

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput, label="Password")
	password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

	class Meta:
		model = CustomUser
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

class PostTipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['content']