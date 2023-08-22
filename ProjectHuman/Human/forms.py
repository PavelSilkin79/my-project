from django import forms
from .models import Profession, Human
import re
from django.core.exceptions import ValidationError

class HumanForm(forms.Form):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = Human
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'profession']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
                }),
            'profession': forms.Select(attrs={
                'class': 'form-control'
                }),
        }
    # title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    # content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5
    # }))
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия', empty_label='Выберите профессию', widget=forms.Select(attrs={
    #     'class': 'form-control'
    # }))
