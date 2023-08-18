from django import forms
from django.core.exceptions import ValidationError
from .models import *

class AddSolutionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['solution'].empty_label = "Не указано"
        self.fields['org_referal'].empty_label = "Не указана"
        self.fields['woman_pasport_type'].empty_label = "Не указан"
        self.fields['man_pasport_type'].empty_label = "Не указан"

    class Meta:
        model = Solution
        fields = [
            'number',
            'commission_name',
            'solution',
            'org_referal',
            'reason',
            'commission_chairman',
            'commission_secretary',
            'commission_members',
            'woman_surname',
            'woman_name',
            'woman_dad_name',
            'woman_birth_date',
            'woman_birth_place',
            'woman_location',
            'woman_pasport_type',
            'woman_pasport_serial',
            'woman_pasport_number',
            'woman_date_issue',
            'woman_issuing_authority',
            'woman_who_issued',
            'man_surname',
            'man_name',
            'man_dad_name',
            'man_birth_date',
            'man_birth_place',
            'man_location',
            'man_pasport_type',
            'man_pasport_serial',
            'man_pasport_number',
            'man_date_issue',
            'man_issuing_authority',
            'man_who_issued',
            'marriage_reg_mark',
        ]
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-input'}),
            'commission_name': forms.TextInput(attrs={'class': 'form-input'}),
            'solution': forms.Select(attrs={'class': 'form-input'}),
            'org_referal': forms.Select(attrs={'class': 'form-input'}),
            'reason': forms.Textarea(attrs={'class': 'form-input'}),
            'commission_chairman': forms.TextInput(attrs={'class': 'form-input'}),
            'commission_secretary': forms.TextInput(attrs={'class': 'form-input'}),
            'commission_members': forms.Textarea(attrs={'class': 'form-input'}),
            'woman_surname': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_name': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_dad_name': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_birth_date': forms.DateInput(attrs={'class': 'form-input'}),
            'woman_birth_place': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_location': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_pasport_type': forms.Select(attrs={'class': 'form-input'}),
            'woman_pasport_serial': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_pasport_number': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_date_issue': forms.DateInput(attrs={'class': 'form-input'}),
            'woman_issuing_authority': forms.TextInput(attrs={'class': 'form-input'}),
            'woman_who_issued': forms.TextInput(attrs={'class': 'form-input'}),
            'man_surname': forms.TextInput(attrs={'class': 'form-input'}),
            'man_name': forms.TextInput(attrs={'class': 'form-input'}),
            'man_dad_name': forms.TextInput(attrs={'class': 'form-input'}),
            'man_birth_date': forms.DateInput(attrs={'class': 'form-input'}),
            'man_birth_place': forms.TextInput(attrs={'class': 'form-input'}),
            'man_location': forms.TextInput(attrs={'class': 'form-input'}),
            'man_pasport_type': forms.Select(attrs={'class': 'form-input'}),
            'man_pasport_serial': forms.TextInput(attrs={'class': 'form-input'}),
            'man_pasport_number': forms.TextInput(attrs={'class': 'form-input'}),
            'man_date_issue': forms.DateInput(attrs={'class': 'form-input'}),
            'man_issuing_authority': forms.TextInput(attrs={'class': 'form-input'}),
            'man_who_issued': forms.TextInput(attrs={'class': 'form-input'}),
            'marriage_reg_mark': forms.TextInput(attrs={'class': 'form-input'}),
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError('Длина превышает 200 символов')
    #
    #     return title