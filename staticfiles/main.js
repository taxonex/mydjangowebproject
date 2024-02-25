// navbar
    //if user icon click to open buttons

    const sign = document.getElementById('sign');
var check = window.getComputedStyle(sign);
function displog(){
  if (check.display === 'none'){
    sign.style.display="block";
  }
  else if (check.display === 'block'){
    sign.style.display="none";
  }
}


//navresponsive
const menuBtn = document.querySelector('.menu-btn');
let nav = document.querySelector('#navBar');
const closeIcon = document.querySelector('.close-icon');

menuBtn.addEventListener('click', function(){
  nav.classList.toggle('nav-open');
})


//login
//animation
document.addEventListener('DOMContentLoaded', function() {
  var animatedElement = document.querySelector('.page-animation1');

  window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var elementOffset = animatedElement.offsetTop;

    // Adjust this value based on when you want the animation to start
    var triggerOffset = 300;

    if (scrollPosition > elementOffset - triggerOffset) {
      animatedElement.style.opacity = 1;
      animatedElement.style.transform = 'scale(1)';
    }
  });
});
document.addEventListener('DOMContentLoaded', function() {
  var animatedElement = document.querySelector('.page-animation');

  window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var elementOffset = animatedElement.offsetTop;

    // Adjust this value based on when you want the animation to start
    var triggerOffset = 300;

    if (scrollPosition > elementOffset - triggerOffset) {
      animatedElement.style.opacity = 1;
      animatedElement.style.transform = 'scale(1)';
    }
  });
});