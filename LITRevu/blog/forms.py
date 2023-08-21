from django import forms
from django.urls import reverse_lazy
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        success_url = reverse_lazy("blog:flux")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "body", "rating"]
        success_url = reverse_lazy("blog:flux")

    # Set rating field to not required
    rating = forms.IntegerField(
        required=False,
        widget=forms.RadioSelect(choices=[(i, str(i)) for i in range(6)]),
    )


class FollowUserForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = "__all__"
        success_url = reverse_lazy("blog:subscriptions")
