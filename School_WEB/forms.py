from django import forms

from School_API.views import Communication,Parent, Student


class CommunicationForm(forms.ModelForm):

    class Meta:
        model = Communication
        fields = '__all__'


class InscriptionParentForm(forms.ModelForm):

    class Meta:
        model= Parent
        fields = '__all__'

class InscriptionStudentForm(forms.ModelForm):

    class Meta:
        model= Student
        fields = '__all__'
