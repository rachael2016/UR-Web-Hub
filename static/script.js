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
const dateschedule = new Date();
if ( (dateschedule.getMonth() > 08) || (dateschedule.getMonth() == 07 && dateschedule.getDate == 31) ) {
    document.getElementById("fall_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Fall 2022 Hours of Operation" + "</span>";
  // sunday (0th day)
    if (dateschedule.getDay() == 0) {
    //pit and rocky's
        if( (dateschedule.getHours() >= 10 || 22)) {
            document.getElementById("fall_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "The Pit" + "</span>";
        }
    //starbucks
        if ( (dateschedule.getHours() >= 8 || dateschedule.getHours() <= 23)) {
            document.getElementById("starbucks_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Starbucks" + "</span>";
        }
    //connections
        if ( (dateschedule.getHours() >= 13 || dateschedule.getHours() <= 20)) {
            document.getElementById("connections_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Connections" + "</span>";
        }
    //hillside
        if ( (dateschedule.getHours() >= 12 || dateschedule.getHours() <= 2)) {
            document.getElementById("hillside_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Hillside" + "</span>";
        }
    //douglass - breakfast
        if ( (dateschedule.getHours() >= 7 && (dateschedule.getHours() <= 9 && dataschedule.getMinutes <= 30)) ){
            document.getElementById("douglass_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Douglass - Breakfast" + "</span>";
        }
    //douglass - brunch 
        if( (dateschedule.getHours() >= 10 && dateschedule.getMinutes() >= 30) && (dateschedule.getHours() <= 14 && dataschedule.getMinutes <= 30) ){
            document.getElementById("douglassbrunch_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Douglass - Brunch" + "</span>";
        }
    //douglass - dinner    
        if ( (dateschedule.getHours() >= 17 || dateschedule.getHours() <= 20)) {
            document.getElementById("douglassdinner_schedule").innerHTML = "<span style='font-family: Century Gothic; display: block; text-align: center; font-weight: bold; color: #ffdb4d; padding-top: 2em; padding-bottom: 2em;'>" + "Douglass - Dinner" + "</span>";
    }
  }
}


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
