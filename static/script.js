//Emersyn, Rachael, Sarah, Kelly, Grant
function openAccordion(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
// display the current date/time 
const dayoftheweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const monthoftheyear = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const date = new Date();
let day = dayoftheweek[date.getDay()];
let month = monthoftheyear[date.getMonth()];
let numberdate = date.getDate();
let hour = date.getHours(); 
let minutes = date.getMinutes();
document.getElementById("current_date").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + day + "," + "&nbsp;" + month + "&nbsp;" + numberdate + "&nbsp;" + hour + ":" + minutes + "</span>";

//then check it against the dining schedule 


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropFunction() {
    document.getElementById("dropMenu").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

document.getElementById("submitSearch").onclick = function () {
    var courseID = document.getElementById("search").value;
    location.href = "/courseratings/" + courseID;
};

var textBox = document.getElementById("search");
var button = document.getElementById("submitSearch");
textBox.addEventListener("keyup", function (event) {
    // Checking if key pressed is ENTER or not
    // if the key pressed is ENTER
    // click listener on button is called
    if (event.keyCode == 13) {
        button.click();
    }
});

document.getElementById("rateThis").onclick = function () {
    location.href = "/coursefeedbackform";
    //Need to also send courseID
};

/*
//Yes to also submitting review
document.getElementById("submitReview").onclick = function () {
    location.href = "/coursefeedbackform";
    //Need to also send courseID
};

//No to also submitting review
document.getElementById("submitAdd").onclick = function () {
    location.href = "/courseratings/" + courseID;
    //Need to also send courseID
};
*/
