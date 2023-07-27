from django.contrib import admin
from blog.models import Ticket, Review


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'time_created', 'user')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'user', 'rating', 'headline', 'body', 'time_created')
    

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
