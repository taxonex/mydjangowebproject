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


const customMenu = document.getElementById('customMenu');

// Handle right-click event
document.addEventListener('contextmenu', (event) => {
  event.preventDefault(); // Prevent default browser context menu

  // Show custom context menu at the mouse position
  customMenu.style.left = event.pageX + 'px';
  customMenu.style.top = event.pageY + 'px';
  customMenu.style.display = 'flex';
});

// Hide custom context menu when clicking elsewhere on the document
document.addEventListener('click', () => {
  customMenu.style.display = 'none';
});

// Handle custom action when the button is clicked
function customAction() {
  alert('Custom action triggered!');
  customMenu.style.display = 'none'; // Hide the context menu
}
