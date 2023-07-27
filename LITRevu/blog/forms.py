from django import forms
from django.urls import reverse_lazy
from . import models

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        success_url = reverse_lazy('blog:home')

class TicketFormDelete(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'body', 'rating']
        success_url = reverse_lazy('blog:home')

class ReviewFormDelete(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)