//Emersyn, Rachael, Sarah, Kelly, Grant
function openAccordion(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

// open image in new tab with big dimensions 
const img = document.getElementById('hoursofop');

img.addEventListener('dblclick', (e) => {
    window.open("/static/hoursofoperation.png")
});

// display the current date/time 
const dayoftheweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const monthoftheyear = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const date = new Date();
let day = dayoftheweek[date.getDay()];
let month = monthoftheyear[date.getMonth()];
let numberdate = date.getDate();
let hour = date.getHours(); 
let minutes = date.getMinutes();
document.getElementById("current_date").innerHTML = day + "," + "&nbsp;" + month + "&nbsp;" + numberdate + "&nbsp;" + hour + ":" + minutes;

//then check against the dining schedule hours
const dateschedule = new Date();
// new schedule for finals week hours
if ((dateschedule.getMonth() == 12) && (dateschedule.getDate() >= 15 && dateschedule.getDate() <= 23)) {
    document.getElementById("finalsweek_schedule").innerHTML = "Reading Period/Final Exam Week Hours of Operation";
    if (dateschedule.getDay() == 4) {
    //thursday 
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 11)) {
            document.getElementById("pit_schedule").innerHTML = "The Pit - Until 11PM";
        }
        if ((dateschedule.getHours() < 23 && (dateschedule.getHours() > 11))) {
            document.getElementById("rockys_schedule").innerHTML = "Rocky's - Until 11PM";
        }
        if ((dateschedule.getHours() <= 23 && (dateschedule.getHours() > 7 || (dateschedule.getHours() = 7 && dateschedule.getMinutes() >= 30)))) {
            document.getElementById("starbucks_schedule").innerHTML = "Starbucks - Until Midnight";
        }
        if ((dateschedule.getHours() >= 11 && dateschedule.getHours() < 22)) {
            document.getElementById("hillside_schedule").innerHTML = "Hillside - Until 10PM";
        }
        if (((dateschedule.getHours() > 8 && dateschedule.getHours() < 14) || (dateschedule.getHours() = 7 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 14 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("peets_schedule").innerHTML = "Peets - Open Until 2:30";
        }
        if ((dateschedule.getHours() >= 7 && dateschedule.getHours() < 10) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("douglassbreak_schedule").innerHTML = "Douglass - Breakfast Until 10:30";
        }
        if (((dateschedule.getHours() > 11 && dateschedule.getHours() < 15) || (dateschedule.getHours() = 11 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 15 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("douglasslunch_schedule").innerHTML = "Douglass - Lunch Until 3:30";
        }
        if ((dateschedule.getHours() >= 17 && dateschedule.getHours() < 21)) {
            document.getElementById("danforthdinner_schedule").innerHTML = "Danforth - Dinner Until 9PM";
        }
        if ((dateschedule.getHours() >= 7 && dateschedule.getHours() < 21)) {
            document.getElementById("connections_schedule").innerHTML = "Connections - Until 9PM";
        }
        if ((dateschedule.getHours() >= 11 && dateschedule.getHours() <= 13) || (dateschedule.getHours() = 13 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("danforthlunch_schedule").innerHTML = "Danforth - Lunch Until 1:30PM";
        }
        if ((dateschedule.getHours() >= 17 && dateschedule.getHours() < 19)) {
            document.getElementById("danforthdinner_schedule").innerHTML = "Danforth - Dinner Until 7PM";
        } else {
            document.getElementById("nothing").innerHTML = "Nothing open";
        }
}
    //friday 
    if (dateschedule.getDay() == 5) {
        if ((dateschedule.getHours() < 18 && dateschedule.getHours() > 11)) {
            document.getElementById("pit_schedule").innerHTML = "The Pit - Until 6PM";
        }
        if ((dateschedule.getHours() < 18 && (dateschedule.getHours() > 7 || (dateschedule.getHours() = 7 && dateschedule.getMinutes() >= 30)))) {
            document.getElementById("starbucks_schedule").innerHTML = "Starbucks - Until 6PM";
        }
        if ((dateschedule.getHours() >= 11 && dateschedule.getHours() < 15)) {
            document.getElementById("hillside_schedule").innerHTML = "Hillside - Until 3PM";
        }
        if (((dateschedule.getHours() > 8 && dateschedule.getHours() < 14) || (dateschedule.getHours() = 7 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 14 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("peets_schedule").innerHTML = "Peets - Open Until 2:30";
        }
        if ((dateschedule.getHours() >= 7 && dateschedule.getHours() < 10) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("douglassbreak_schedule").innerHTML = "Douglass - Breakfast Until 10:30";
        }
        if (((dateschedule.getHours() > 11 && dateschedule.getHours() < 15) || (dateschedule.getHours() = 11 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 15 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("douglasslunch_schedule").innerHTML = "Douglass - Lunch Until 3:30";
        } else {
        document.getElementById("nothing").innerHTML = "Nothing open";
    }
}
    //saturday 
    if (dateschedule.getDay() == 6) {
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 10)) {
            document.getElementById("pit_schedule").innerHTML = "The Pit - Until 11PM";
        }
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 10)) {
            document.getElementById("rockys_schedule").innerHTML = "Rocky's - Until 11PM";
        }
        if ((dateschedule.getHours() <= 23 && dateschedule.getHours() > 9 || (dateschedule.getHours() = 0))) {
            document.getElementById("starbucks_schedule").innerHTML = "Starbucks - Until 1AM";
        }
        if ((dateschedule.getHours() < 2 || (dateschedule.getHours() >= 12 && dateschedule.getHours() <= 23))) {
            document.getElementById("hillside_schedule").innerHTML = "Hillside - Until 2AM";
        }
        if ((dateschedule.getHours() >= 8 && dateschedule.getHours() < 10) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("danforthbreak_schedule").innerHTML = "Danforth - Breakfast Until 10AM";
        }
        if (((dateschedule.getHours() >= 11 && dateschedule.getHours() < 14) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 14 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("danforthlunch_schedule").innerHTML = "Danforth - Brunch Until 2:30PM";
        }
        if ((dateschedule.getHours() >= 17 && dateschedule.getHours() < 20)) {
            document.getElementById("danforthdinner_schedule").innerHTML = "Danforth - Dinner Until 8PM";
        } else {
            document.getElementById("nothing").innerHTML = "Nothing open";
        }
}
    //sunday 
    if (dateschedule.getDay() == 0) {
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 10)) {
            document.getElementById("pit_schedule").innerHTML = "The Pit - Until 11PM";
        }
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 10)) {
            document.getElementById("rockys_schedule").innerHTML = "Rocky's - Until 11PM";
        }
        if ((dateschedule.getHours() <= 23 && dateschedule.getHours() >= 9)) {
            document.getElementById("starbucks_schedule").innerHTML = "Starbucks - Until Midnight";
        }
        if ((dateschedule.getHours() < 1 || (dateschedule.getHours() >= 12 && dateschedule.getHours() <= 23))) {
            document.getElementById("hillside_schedule").innerHTML = "Hillside - Until 1AM";
        }
        if ((dateschedule.getHours() > 7 && dateschedule.getHours() < 10) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("douglassbreak_schedule").innerHTML = "Douglass - Breakfast Until 10:30";
        }
        if (((dateschedule.getHours() >= 11 && dateschedule.getHours() < 14) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 14 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("douglasslunch_schedule").innerHTML = "Douglass - Brunch Until 2:30PM";
        }
        if ((dateschedule.getHours() >= 17 && dateschedule.getHours() < 20)) {
            document.getElementById("douglasshdinner_schedule").innerHTML = "Douglass - Dinner Until 8PM";
        }
        if ((dateschedule.getHours() >= 14 && dateschedule.getHours() < 21)) {
            document.getElementById("connections_schedule").innerHTML = "Connections - Until 9PM";
        } else {
            document.getElementById("nothing").innerHTML = "Nothing open";
        }
}
    //monday - wednesday 
    if (dateschedule.getDay() == 1 || 2 || 3) {
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 10)) {
            document.getElementById("pit_schedule").innerHTML = "The Pit - Until 11PM";
        }
        if ((dateschedule.getHours() < 23 && dateschedule.getHours() > 10)) {
            document.getElementById("rockys_schedule").innerHTML = "Rocky's - Until 11PM";
        }
        if ((dateschedule.getHours() <= 23 && (dateschedule.getHours() > 7 || (dateschedule.getHours() = 7 && dateschedule.getMinutes() >= 30)))) {
            document.getElementById("starbucks_schedule").innerHTML = "Starbucks - Until Midnight";
        }
        if ((dateschedule.getHours() < 1 || (dateschedule.getHours() >= 12 && dateschedule.getHours() <= 23))) {
            document.getElementById("hillside_schedule").innerHTML = "Hillside - Until 1AM";
        }
        if (((dateschedule.getHours() > 8 && dateschedule.getHours() < 14) || (dateschedule.getHours() = 7 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 14 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("peets_schedule").innerHTML = "Peets - Open Until 2:30";
        }
        if ((dateschedule.getHours() >= 7 && dateschedule.getHours() < 10) || (dateschedule.getHours() = 10 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("douglassbreak_schedule").innerHTML = "Douglass - Breakfast Until 10:30";
        }
        if (((dateschedule.getHours() > 11 && dateschedule.getHours() < 15) || (dateschedule.getHours() = 11 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 15 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("douglasslunch_schedule").innerHTML = "Douglass - Lunch Until 3:30";
        } 
        if ((dateschedule.getHours() >= 17 && dateschedule.getHours() < 21)) {
            document.getElementById("danforthdinner_schedule").innerHTML = "Danforth - Dinner Until 9PM";
        }   
        if ((dateschedule.getHours() >= 7 && dateschedule.getHours() < 21)) {
            document.getElementById("connections_schedule").innerHTML = "Connections - Until 9PM";
        }
        if ((dateschedule.getHours() >= 11 && dateschedule.getHours() <= 13) || (dateschedule.getHours() = 13 && dateschedule.getMinutes() <= 30)) {
            document.getElementById("danforthlunch_schedule").innerHTML = "Danforth - Lunch Until 1:30PM";
        }
        if ((dateschedule.getHours() >= 17 && dateschedule.getHours() < 19)) {
            document.getElementById("danforthdinner_schedule").innerHTML = "Danforth - Dinner Until 7PM";
        }
        if (((dateschedule.getHours() > 11 && dateschedule.getHours() < 13) || (dateschedule.getHours() = 11 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 13 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("brew_schedule").innerHTML = "The Brew @ Simon - Open Until 1:30PM";
        }
        if (((dateschedule.getHours() > 11 && dateschedule.getHours() < 13) || (dateschedule.getHours() = 11 && dateschedule.getMinutes() >= 30) || (dateschedule.getHours() = 13 && dateschedule.getMinutes() <= 30))) {
            document.getElementById("facultyclub_schedule").innerHTML = "Faculty Club - Open Until 1:30";
        } else {
            document.getElementById("nothing").innerHTML = "Nothing open";
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
    location.href = "rmc_feedback";
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
