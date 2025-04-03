document.addEventListener("DOMContentLoaded", function() {
    let errorElements = document.querySelectorAll('.error');
    errorElements.forEach(errorElement =>  {
        if (error.textContent.trim() !== '') {
            error.classList.add("show");
        }
        });
});