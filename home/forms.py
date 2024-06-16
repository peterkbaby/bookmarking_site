from django.forms import ModelForm
from .models import books

class BookForm(ModelForm):
    class Meta:
        model = books
        fields = ("title","url","important")
