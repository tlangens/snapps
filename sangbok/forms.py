from django import forms
from django.db import models
from django.core.validators import RegexValidator
from sangbok.models import Snapsvisa, Category
from django.utils.translation import ugettext_lazy as _

class SongForm(forms.ModelForm):

    # TODO: Add regex checks

    class Meta:
        model = Snapsvisa
        fields = ('name', 'category', 'lyrics', 'other',)
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'category': forms.widgets.Select(attrs={'class': 'form-control'}),
            'lyrics': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            'other': forms.widgets.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Namn'),
            'other': _('Annat'),
            'category': _('Kategori'),
            'lyrics': _('Text'),
        }

class CategorySelectForm(forms.Form):
    c = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'id': 'category-list'}),
        )