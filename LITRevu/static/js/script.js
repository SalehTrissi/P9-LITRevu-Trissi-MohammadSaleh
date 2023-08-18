document.addEventListener("DOMContentLoaded", function() {
    const critiquesLink = document.getElementById("critiques-link");
    const ticketsLink = document.getElementById("tickets-link");
    const selectedOption = document.getElementById("selected-option");
    const ticketContent = document.getElementsByClassName("is-ticket");
    const reviewContent = document.getElementsByClassName("is-review");
    const allLink = document.getElementById("all-link");
    
    critiquesLink.addEventListener("click", function() {
        selectedOption.textContent = "Critiques";
        for (const ticket of ticketContent) {
            ticket.style.display = "none";
        }
        for (const review of reviewContent) {
            review.style.display = "block";
        }
    });
    
    ticketsLink.addEventListener("click", function() {
        selectedOption.textContent = "Tickets";
        for (const review of reviewContent) {
            review.style.display = "none";
        }
        for (const ticket of ticketContent) {
            ticket.style.display = "block";
        }
    });
    
    allLink.addEventListener("click", function () {
        selectedOption.textContent = "Tous";
        for (const item of ticketContent) {
            item.style.display = "block";
        }
        for (const item of reviewContent) {
            item.style.display = "block";
        }
    });
});
