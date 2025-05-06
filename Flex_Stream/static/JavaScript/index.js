document.addEventListener("DOMContentLoaded", () => {
    const slides = document.getElementById("slides");
    const totalSlides = slides.children.length;
    const dotsContainer = document.getElementById("dots");
    const leftNav = document.getElementById("left-nav");
    const rightNav = document.getElementById("right-nav");
  
    let index = 0;
  
    // Create dots dynamically
    for (let i = 0; i < totalSlides; i++) {
      const dot = document.createElement("span");
      dot.classList.add("dot");
      if (i === 0) dot.classList.add("active");
      dot.dataset.index = i;
      dotsContainer.appendChild(dot);
    }
  
    const dots = document.querySelectorAll(".dot");
  
    function goToSlide(i) {
      index = (i + totalSlides) % totalSlides; // handles negative index
      slides.style.transform = `translateX(-${index * 100}%)`;
  
      dots.forEach(dot => dot.classList.remove("active"));
      dots[index].classList.add("active");
    }
  
    // Dot click event
    dots.forEach(dot => {
      dot.addEventListener("click", () => {
        goToSlide(parseInt(dot.dataset.index));
      });
    });
  
    // Left click
    leftNav.addEventListener("click", () => {
      goToSlide(index - 1);
    });
  
    // Right click
    rightNav.addEventListener("click", () => {
      goToSlide(index + 1);
    });
  });
  