from django import forms
from django.forms import RadioSelect
from django.urls import reverse_lazy
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        success_url = reverse_lazy('blog:flux')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'body', 'rating']
        success_url = reverse_lazy('blog:flux')

        widgets = {
            'rating': RadioSelect(choices=models.Review.RATING_CHOICES, attrs={"class": "form-check-input"})
        }
    # Set rating field to not required
    rating = forms.IntegerField(required=False)


class FollowUserForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = '__all__'
        success_url = reverse_lazy('blog:subscriptions')
