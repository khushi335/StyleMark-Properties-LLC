const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;

function showSlide(index) {
    slides.forEach(s => s.classList.remove('active'));
    dots.forEach(d => d.classList.remove('active'));
    
    slides[index].classList.add('active');
    dots[index].classList.add('active');
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Auto-play every 5 seconds
setInterval(nextSlide, 5000);

// Optional: Manual navigation logic for buttons can be added here



    const modal = document.getElementById("galleryModal");
    const modalImg = document.getElementById("img01");
    const captionText = document.getElementById("caption");
    const closeBtn = document.getElementsByClassName("close-modal")[0];

    function openLightbox(element) {
        const img = element.querySelector('img');
        modal.style.display = "block";
        modalImg.src = img.src;
        captionText.innerHTML = img.alt;
        document.body.style.overflow = "hidden"; // Prevent scrolling when open
    }

    closeBtn.onclick = function() {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            document.body.style.overflow = "auto";
        }
    }