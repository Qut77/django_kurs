from .models import articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class articles_form(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={'class':'form-control custom-input mb-3', 'placeholder': 'Название статьи'}),
            'anons': TextInput(attrs={'class':'form-control custom-input mb-3', 'placeholder': 'Анонс статьи'}),
            'text': Textarea(attrs={'class':'form-control custom-input mb-3', 'placeholder': 'Текст статьи'}),
            'date': DateTimeInput(attrs={'class':'form-control custom-input mb-3', 'placeholder': 'Дата публикации'}),
        }