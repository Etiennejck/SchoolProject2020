from django import forms

from School_API.views import Communication,Parent, Student, Absence, MessageSend


class CommunicationForm(forms.ModelForm):

    class Meta:
        model = Communication
        fields = '__all__'

class MessageSendForm(forms.ModelForm):

    class Meta:
        model = MessageSend
        fields = '__all__'

class InscriptionParentForm(forms.ModelForm):

    class Meta:
        model= Parent
        fields = '__all__'

class InscriptionStudentForm(forms.ModelForm):

    class Meta:
        model= Student
        fields = '__all__'

class AbsenceForm(forms.ModelForm):

    class Meta:
        model = Absence
        fields = '__all__'

class addAbsenceForm(forms.Form):
    document = forms.FileField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    messageAbs = forms.Textarea()
    id_student = forms.IntegerField()