from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from itertools import chain
from authentication.models import User
from .models import Ticket, Review, UserFollows
from django.contrib import messages
from django.core.paginator import Paginator


@login_required
def flux(request):
    flux_ticket = Ticket.objects.all()
    flux_review = Review.objects.all()
    combined_data = sorted(
        chain(flux_ticket, flux_review),
        key=lambda instance: instance.time_created,
        reverse=True,
    )

    p = Paginator(combined_data, 4)
    page_number = request.GET.get("page")
    page = p.get_page(page_number)

    context = {
        "page": page,
    }

    return render(request, "blog/flux.html", context)


@login_required
def posts(request):
    # Filter the Ticket and Review objects for the currently logged-in user
    posts_ticket = Ticket.objects.filter(user=request.user)
    posts_review = Review.objects.filter(user=request.user)
    show_critiques = True
    show_tickets = False

    combined_data = sorted(
        chain(posts_ticket, posts_review),
        key=lambda instance: instance.time_created,
        reverse=True,
    )

    p = Paginator(combined_data, 4)
    # Get the current page number from the query parameter 'page'
    page_number = request.GET.get("page")

    # Paginate the filtered ticket and review data
    page = p.get_page(page_number)

    context = {
        "page": page,
        "show_critiques": show_critiques,
        "show_tickets": show_tickets,
    }

    return render(request, "blog/posts.html", context)


@login_required
def create_ticket(request):
    # If the form is submitted via POST
    if request.method == "POST":
        # Create an instance of the ticket form with the submitted data
        form = forms.TicketForm(request.POST, request.FILES)
        # Check if the form is valid
        if form.is_valid():
            # Save the ticket form to get the ticket object
            ticket = form.save(commit=False)
            # Set the user for the ticket
            ticket.user = request.user
            ticket.save()

            # Display a success message
            messages.success(request, "Ticket créé avec succès.")

            # Redirect to the 'flux' page
            return redirect("blog:flux")
        else:
            # If the form is not valid, display an error message
            messages.error(
                request,
                "Erreur lors de la création du ticket. Veuillez vérifier le formulaire.",
            )
    else:
        # If the request is a GET request (i.e., the user is loading the page),
        # create an instance of an empty ticket form
        form = forms.TicketForm()

    # Pass the ticket form to the template
    context = {
        "form": form,
    }

    # Render the template with the ticket form
    return render(request, "blog/create_ticket.html", context)


@login_required
def create_review(request):
    # If the form is submitted via POST
    if request.method == "POST":
        # Create instances of both ticket and review forms with the submitted data
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)

        # Check if both forms are valids
        if ticket_form.is_valid() and review_form.is_valid():
            # Save the ticket form to get the ticket object
            ticket = ticket_form.save(commit=False)
            # Set the user for the ticket
            ticket.user = request.user
            ticket.save()

            # Save the review without committing to the database
            review = review_form.save(commit=False)
            # Set the user and ticket for the review
            review.user = request.user
            review.ticket = ticket
            # Save the review to the database
            review.save()

            # Redirect to the 'posts' page
            messages.success(request, "Critique créé avec succès.")
            return redirect("blog:posts")
        else:
            messages.error(
                request,
                "Erreur lors de la création une critique. Veuillez vérifier le formulaire.",
            )
    else:
        # If the request is a GET request (i.e., the user is loading the page),
        # create instances of empty ticket and review forms
        ticket_form = forms.TicketForm()
        review_form = forms.ReviewForm()

    # Pass the ticket and review forms to the template
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }

    # Render the template with the forms
    return render(request, "blog/create_review.html", context)


@login_required
def response_review(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            messages.success(request, "Critique créée avec succès.")
            return redirect("blog:flux")
        else:
            messages.error(
                request,
                "Erreur lors de la création d'une critique. Veuillez vérifier le formulaire.",
            )
    else:
        review_form = forms.ReviewForm()

    context = {
        "review_form": review_form,
        "ticket": ticket,
    }

    return render(request, "blog/response_review.html", context)


def model_type(value):
    return type(value).__name__


@login_required
def ticket_detail(request, ticket_id):
    # Get the ticket object with the given ticket_id or return a 404 error page if not found
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Create a context dictionary containing the ticket data
    context = {"ticket": ticket}

    # Render the 'ticket_detail.html' template with the data in the context
    return render(request, "blog/ticket_detail.html", context)


@login_required
def update_ticket(request, ticket_id):
    # Get the ticket object with the given ticket_id or return a 404 error page if not found
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.user != ticket.user:
        return redirect("blog:flux")

    if request.method == "POST":
        # If the request method is POST, process the form data
        form_ticket = forms.TicketForm(request.POST, instance=ticket)

        if form_ticket.is_valid():
            # Save the form data excluding the image field
            updated_ticket = form_ticket.save(commit=False)

            # Check if a new image was uploaded
            if "image" in request.FILES:
                updated_ticket.image = request.FILES["image"]

            updated_ticket.save()

            # Display a success message
            messages.success(request, "Votre ticket est mis à jour avec succès.")

            # Redirect the user to the 'posts' page after successful ticket update
            return redirect("blog:posts")
        else:
            # Display an error message if the form data is not valid
            messages.error(
                request,
                "Erreur lors de la mise à jour du ticket. Veuillez vérifier le formulaire.",
            )
    else:
        # If the request method is GET, create a form instance with the current ticket data
        form_ticket = forms.TicketForm(instance=ticket)

    # Create a context dictionary containing the ticket and the form
    context = {
        "ticket": ticket,
        "form_ticket": form_ticket,
    }

    # Render the 'update_ticket.html' template with the data in the context
    return render(request, "blog/update_ticket.html", context)


@login_required
def update_review(request, review_id):
    # Get the review object with the given review_id or return a 404 error if not found
    review = get_object_or_404(Review, id=review_id)

    # Check if the current user is the owner of the review
    if request.user != review.user:
        # Redirect the user to the 'flux' page or display an error message
        return redirect("blog:flux")

    # If the request method is POST, it means the form is submitted for updating the review
    if request.method == "POST":
        # Create a ReviewForm instance with the submitted POST data and the existing review object
        form_review = forms.ReviewForm(request.POST, instance=review)

        # Check if the form data is valid
        if form_review.is_valid():
            # Save the form data to update the review
            form_review.save()

            # Display a success message indicating that the review was updated successfully
            messages.success(request, "Votre review est mise à jour avec succès")

            # Redirect the user to the 'posts' page after successful update
            return redirect("blog:posts")
    else:
        # If the request method is GET, it means the user is accessing the page to view the form
        # Create a ReviewForm instance with the existing review object to pre-fill the form
        form_review = forms.ReviewForm(instance=review)

    # Prepare the context data to pass to the template
    context = {
        "review": review,
        "form_review": form_review,
    }

    # Render the 'update_review.html' template with the context data
    return render(request, "blog/update_review.html", context)


@login_required
def delete_ticket(request, ticket_id):
    # Get the ticket object with the given ticket_id or return a 404 error if not found
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Check if the current user is the owner of the ticket
    if request.user != ticket.user:
        # Redirect the user to the 'flux' page or display an error message
        return redirect("blog:flux")

    # If the user is the owner of the ticket, proceed to delete it
    ticket.delete()

    # Display a success message indicating that the ticket was deleted successfully
    messages.success(request, "Votre ticket est supprimée avec succès")

    # Redirect the user to the 'posts' page after successful deletion
    return redirect("blog:posts")


@login_required
def delete_review(request, review_id):
    # Get the review object with the given review_id or return a 404 error if not found
    review = get_object_or_404(Review, id=review_id)

    # Check if the current user is the owner of the review
    if request.user != review.user:
        return redirect("blog:flux")

    # If the user is the owner of the review, proceed to delete it
    review.delete()

    messages.success(request, "Votre review est supprimée avec succès")

    return redirect("blog:posts")


@login_required
def subscriptions(request):
    # Create a form instance for following other users
    subscriptions_form = forms.FollowUserForm()

    # Get the objects that represent the users that the current user is following
    subscriptions_objects = UserFollows.objects.filter(user=request.user)

    # Get the objects that represent the users who are following the current user
    subscribers_objects = UserFollows.objects.filter(followed_user=request.user)

    # Prepare the context with the subscriptions and following users
    context = {
        "subscriptions_form": subscriptions_form,
        "subscriptions_objects": subscriptions_objects,
        "subscribers_objects": subscribers_objects,
    }

    # Redirect the user to the 'subscriptions' page
    return render(request, "blog/subscriptions.html", context)


@login_required
def search_user(request):
    if request.method == "POST":
        # Get the value of the 'searched' input field from the POST data
        searched = request.POST.get("searched")

        # Filter the User objects whose usernames contain the searched value
        users = User.objects.filter(username__contains=searched)

        # Get the list of user IDs that the logged-in user is following
        following_users = UserFollows.objects.filter(user=request.user).values_list(
            "followed_user__id", flat=True
        )

        # Prepare the context with the search results and following users
        context = {
            "searched": searched,
            "users": users,
            "following_users": following_users,
        }

        # Display a success message when the user is successfully searched for
        if searched and users.exists():
            messages.success(request, f'Recherche réussie pour "{searched}".')

        # Render the 'search_user.html' template with the context
        return render(request, "blog/search_user.html", context)

    # If it's not a POST request, just render the 'search_user.html' template with an empty context
    return render(request, "blog/search_user.html", {})


@login_required
def subscribe_user(request, user_id):
    # Get the User object to be followed
    followed_user = get_object_or_404(User, id=user_id)

    # Check if the logged-in user is not already following the user
    if not UserFollows.objects.filter(
        user=request.user, followed_user=followed_user
    ).exists():
        # Create a new UserFollows object to represent the subscription
        UserFollows.objects.create(user=request.user, followed_user=followed_user)

        # Set the success message for the user
        message = f"Vous êtes maintenant abonné à {followed_user.username}."
    else:
        # Set the warning message for the user
        message = f"Vous êtes déjà abonné à {followed_user.username}."

    # Display the appropriate message to the user
    messages.success(request, message)

    # Redirect the user to the 'subscriptions' page
    return redirect("blog:subscriptions")


@login_required
def unsubscribe_user(request, user_id):
    # Get the User object to be unfollowed
    followed_user = get_object_or_404(User, id=user_id)

    # Check if the logged-in user is following the user
    if UserFollows.objects.filter(
        user=request.user, followed_user=followed_user
    ).exists():
        # Delete the UserFollows object representing the subscription
        UserFollows.objects.filter(
            user=request.user, followed_user=followed_user
        ).delete()

        # Set the warning message for the user
        message = f"Vous vous êtes désabonné de {followed_user.username}."
    else:
        # Set the warning message for the user
        message = f"Vous n'êtes pas abonné à {followed_user.username}."

    # Display the appropriate message to the user
    messages.warning(request, message)

    # Redirect the user to the 'subscriptions' page
    return redirect("blog:subscriptions")
