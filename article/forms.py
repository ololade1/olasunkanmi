from django import forms
from .import models


class CreateClient(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title','slug','body','thumb']