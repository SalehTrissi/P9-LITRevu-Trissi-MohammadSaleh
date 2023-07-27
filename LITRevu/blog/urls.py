from django.urls import path
from .views import home, create_ticket, create_ticket_and_review, edit_ticket, edit_review

urlpatterns = [
    path('', home, name='home'),
    path('ticket/create/', create_ticket, name='create-ticket'),
    path('review/create/', create_ticket_and_review, name='create-review'),
    path('ticket/edit/<int:ticket_id>', edit_ticket, name='edit-ticket'),
    path('review/edit/<int:review_id>', edit_review, name='edit-review'),

]