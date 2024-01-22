function initializeSlider(selector, slides) {
    let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'block' : 'none';
        });
    }

    document.getElementById(`${selector}_left`).addEventListener('click', () => {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    });

    document.getElementById(`${selector}_right`).addEventListener('click', () => {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    });

    showSlide(currentSlide);
}

const slides = document.querySelectorAll('.slide_img');
const slides2 = document.querySelectorAll('.slide_img_2');
const slides3 = document.querySelectorAll('.slide_img_3');
const slides4 = document.querySelectorAll('.slide_img_4');
const slides5 = document.querySelectorAll('.slide_img_5');
const slides6 = document.querySelectorAll('.slide_img_6');

initializeSlider('post_1', slides);
initializeSlider('post_2', slides2);
initializeSlider('post_3', slides3);
initializeSlider('post_4', slides4);
initializeSlider('post_5', slides5);
initializeSlider('post_6', slides6);