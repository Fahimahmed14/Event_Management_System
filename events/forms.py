from django import forms
from .models import Event, Participant, Category


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border focus:ring-4 focus:ring-indigo-300 outline-none'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border focus:ring-4 focus:ring-indigo-300 outline-none'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 rounded-xl border focus:ring-4 focus:ring-indigo-300 outline-none'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border focus:ring-4 focus:ring-indigo-300 outline-none'
            }),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'