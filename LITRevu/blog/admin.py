from django.contrib import admin
from blog.models import Ticket, Review, UserFollows


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'time_created', 'user')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'user', 'rating', 'headline', 'body', 'time_created')
    

class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'followed_user')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)