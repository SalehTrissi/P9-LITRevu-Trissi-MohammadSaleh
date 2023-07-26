from django.contrib import admin
from blog.models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'time_created', 'user')


admin.site.register(Ticket, TicketAdmin)