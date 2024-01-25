function initializeSlider(selector, slides) {
    let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'block' : 'none';
        });
    }
    showSlide(currentSlide);
       // document.getElementById(`post_1_left`).addEventListener('click', () => {
       //     currentSlide = (currentSlide - 1 + slides.length) % slides.length;
       //     showSlide(currentSlide);
       // });
//
      //  document.getElementById(`${selector}_right`).addEventListener('click', () => {
      //      currentSlide = (currentSlide + 1) % slides.length;
      //      showSlide(currentSlide);
      //  });
    
    
}

const slides1 = document.querySelectorAll('.slide_img_1');
const slides2 = document.querySelectorAll('.slide_img_2');
const slides3 = document.querySelectorAll('.slide_img_3');
const slides4 = document.querySelectorAll('.slide_img_4');
const slides5 = document.querySelectorAll('.slide_img_5');
const slides6 = document.querySelectorAll('.slide_img_6');
const slides7 = document.querySelectorAll('.slide_img_7');
const slides8 = document.querySelectorAll('.slide_img_8');
const slides9 = document.querySelectorAll('.slide_img_9');
const slides10 = document.querySelectorAll('.slide_img_10');
const slides11 = document.querySelectorAll('.slide_img_11');
const slides12 = document.querySelectorAll('.slide_img_12');
const slides13 = document.querySelectorAll('.slide_img_13');

initializeSlider('post_1', slides1);
initializeSlider('post_2', slides2);
initializeSlider('post_3', slides3);
initializeSlider('post_4', slides4);
initializeSlider('post_5', slides5);
initializeSlider('post_6', slides6);
initializeSlider('post_7', slides7);
initializeSlider('post_8', slides8);
initializeSlider('post_9', slides9);
initializeSlider('post_10', slides10);
initializeSlider('post_11', slides11);
initializeSlider('post_12', slides12);
initializeSlider('post_13', slides13);