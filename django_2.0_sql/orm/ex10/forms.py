from django import forms
from .models import People

class Ex10Form(forms.Form):
	min_date = forms.DateField(label="Movies minimum release date", widget=forms.DateInput(attrs={'type': 'date'}))
	max_date = forms.DateField(label="Movies maximum release date", widget=forms.DateInput(attrs={'type': 'date'}))
	min_diameter = forms.IntegerField(label="Planet diameter greater than")
	gender = forms.ChoiceField(label="Character gender", choices=[])


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		genders = People.objects.values_list("gender", flat=True).distinct()
		self.fields["gender"].choices = [(gender, gender) for gender in genders if gender]		