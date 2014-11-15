from django import forms
from .models import categoria

class categoriaForm(forms.ModelForm):

   class Meta:
      model = categoria