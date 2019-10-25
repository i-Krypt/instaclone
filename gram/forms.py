from django import forms

from .models import Book

class BookForm(forms.modelsForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf')