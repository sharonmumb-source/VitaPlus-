// Smooth button scroll (optional future use)
document.addEventListener("DOMContentLoaded", function () {
    const cta = document.querySelector(".cta-btn");

    if (cta) {
        cta.addEventListener("click", () => {
            window.location.href = "/benefits/";
        });
    }
});

// Navbar shadow on scroll
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {
        navbar.style.boxShadow = "0 4px 15px rgba(0,0,0,0.1)";
    } else {
        navbar.style.boxShadow = "0 2px 10px rgba(0,0,0,0.05)";
    }
});
