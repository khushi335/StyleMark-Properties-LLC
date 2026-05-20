// --- Slide Logic ---
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;

function showSlide(index) {
    if (slides.length === 0 || dots.length === 0) return; // Guard clause
    slides.forEach(s => s.classList.remove('active'));
    dots.forEach(d => d.classList.remove('active'));
    
    slides[index].classList.add('active');
    dots[index].classList.add('active');
}

function nextSlide() {
    if (slides.length === 0) return;
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

if (slides.length > 0) {
    setInterval(nextSlide, 5000);
}

// --- Lightbox / Modal Logic (Fixed & Guarded) ---
document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("galleryModal");
    const modalImg = document.getElementById("img01");
    const captionText = document.getElementById("caption");
    const closeBtn = document.getElementsByClassName("close-modal")[0];

    // Global function wrapper so it can still be called inline from HTML
    window.openLightbox = function(element) {
        if (!modal || !modalImg) return;
        const img = element.querySelector('img');
        modal.style.display = "block";
        modalImg.src = img.src;
        if (captionText && img.alt) {
            captionText.innerHTML = img.alt;
        }
        document.body.style.overflow = "hidden"; // Prevent scrolling when open
    };

    // Only bind events if the elements are present on the current page template
    if (closeBtn) {
        closeBtn.onclick = function() {
            if (modal) modal.style.display = "none";
            document.body.style.overflow = "auto";
        };
    }

    window.onclick = function(event) {
        if (modal && event.target == modal) {
            modal.style.display = "none";
            document.body.style.overflow = "auto";
        }
    };
});