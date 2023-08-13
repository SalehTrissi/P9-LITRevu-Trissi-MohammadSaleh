from django.contrib import admin
from blog.models import Ticket, Review, UserFollows


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "time_created", "user")


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ticket_title",
        "ticket_image",
        "ticket_description",
        "user",
        "rating",
        "headline",
        "body",
        "time_created",
    )

    def ticket_title(self, obj):
        return obj.ticket.title

    def ticket_image(self, obj):
        return obj.ticket.image

    def ticket_description(self, obj):
        return obj.ticket.description


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "followed_user")


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
