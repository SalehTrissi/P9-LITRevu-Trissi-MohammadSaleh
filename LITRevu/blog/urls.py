from django.urls import path
from .views import home, TicketCreateView

urlpatterns = [
    path('', home, name='home'),
    path('tickets/create/', TicketCreateView.as_view(), name='create-ticket')
]