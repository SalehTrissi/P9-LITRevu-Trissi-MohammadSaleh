document.addEventListener("DOMContentLoaded", function() {
    const critiquesLink = document.getElementById("critiques-link");
    const ticketsLink = document.getElementById("tickets-link");
    const selectedOption = document.getElementById("selected-option");
    const ticketContent = document.getElementById("is-ticket");
    const reviewContent = document.getElementById("is-review");
    const allLink = document.getElementById("all-link")
    
    critiquesLink.addEventListener("click", function() {
        selectedOption.textContent = "Critiques";
        ticketContent.style.display = "none";
        reviewContent.style.display = "block";
    });
    
    ticketsLink.addEventListener("click", function() {
        selectedOption.textContent = "Tickets";
        reviewContent.style.display = "none";
        ticketContent.style.display = "block";
    });
    allLink.addEventListener("click", function () {
        selectedOption.textContent = "Tous";
        ticketContent.style.display = "block";
        reviewContent.style.display = "block";
    })
});
