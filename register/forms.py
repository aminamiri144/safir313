from django import forms
from .models import Kid


class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(KidForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'