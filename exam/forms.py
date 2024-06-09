from django import forms
from .models import QuestionBank

class QuestionBankForm(forms.ModelForm):
    class Meta:
        model = QuestionBank
        fields = '__all__'
