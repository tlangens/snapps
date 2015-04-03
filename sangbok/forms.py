from django import forms
from django.db import models
from django.core.validators import RegexValidator
from sangbok.models import Snapsvisa, Category
from django.utils.translation import ugettext_lazy as _

class SongForm(forms.ModelForm):

    # TODO: Add regex checks

    class Meta:
        model = Snapsvisa
        fields = ('name', 'category', 'lyrics', 'pre', 'post',)
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'category': forms.widgets.Select(attrs={'class': 'form-control'}),
            'lyrics': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            'pre': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            'post': forms.widgets.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Namn'),
            'pre': _('Förord'),
            'category': _('Kategori'),
            'lyrics': _('Text'),
            'post': _('Efterord'),
        }

class CategorySelectForm(forms.Form):
    c = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'id': 'category-list'}),
        )