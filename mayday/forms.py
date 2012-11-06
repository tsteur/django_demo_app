from mayday.models import BookCollectionInline
from django import forms


class BookCollectionInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookCollectionInlineForm, self).__init__(*args, **kwargs)
        self.fields['position'].widget = forms.HiddenInput()

    class Meta:
        model = BookCollectionInline
