from django.urls import path
from . import views


urlpatterns = [
    path("", views.flux, name="flux"),
    path("posts/", views.posts, name="posts"),
    path("create_ticket/", views.create_ticket, name="create-ticket"),
    path("create_review/", views.create_review, name="create-review"),
    path("update_ticket/<int:ticket_id>/", views.update_ticket, name="update-ticket"),
    path("delete_ticket/<int:ticket_id>/", views.delete_ticket, name="delete-ticket"),
    path("delete_review/<int:review_id>/", views.delete_review, name="delete-review"),
    path("update_review/<int:review_id>/", views.update_review, name="update-review"),
    path("search_user/", views.search_user, name="search-user"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("subscribe/<int:user_id>/", views.subscribe_user, name="subscribe"),
    path("unsubscribe/<int:user_id>/", views.unsubscribe_user, name="unsubscribe"),
    path("response_review/<int:ticket_id>/", views.response_review, name="response-review"),
]
