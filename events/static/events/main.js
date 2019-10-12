$(document).ready(function(){
  $("p").click(function(){
    alert("The paragraph was clicked.");
  });
});

function pageLoaded() {
    document.querySelectorAll(".single-event").forEach(el => {el.style.opacity = 1});
}
window.onload = pageLoaded;

