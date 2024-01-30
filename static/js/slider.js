function initializeSlider(selector, slides) { 
   let currentSlide = 0;

   function showSlide(index) {
       slides.forEach((slide, i) => {
           slide.style.display = i === index ? 'block' : 'none';
       });
   }
   document.querySelector(`#${selector}_left`).addEventListener('click', () => {
       currentSlide = (currentSlide - 1 + slides.length) % slides.length;
       showSlide(currentSlide);
   });

   document.getElementById(`${selector}_right`).addEventListener('click', () => {
       currentSlide = (currentSlide + 1) % slides.length;
       showSlide(currentSlide);
   });

   showSlide(currentSlide);

}

const post = document.querySelectorAll('.post')

post.forEach((el, index)=>{
    initializeSlider(`post_${index+1}`,
    document.querySelectorAll(`.slide_img_${index+1}`))
})



