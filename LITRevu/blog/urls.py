from django.urls import path
from .views import home, TicketCreateView, ReviewCreateView

urlpatterns = [
    path('', home, name='home'),
    path('ticket/create/', TicketCreateView.as_view(), name='create-ticket'),
    path('review/create/', ReviewCreateView.as_view(), name='create-review')
]