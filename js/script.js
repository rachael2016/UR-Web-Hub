function openAccordion(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

date = new Date().toLocaleString();
document.getElementById("current_date").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + date + "</span>";