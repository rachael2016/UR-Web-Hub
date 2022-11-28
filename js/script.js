function openAccordion(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

function openResponsiveMenu() {
  var x = document.getElementById("navMenu");
  if (x.className === "menu") {
    x.className += " responsive";
  } else {
    x.className = "menu";
  }
} 