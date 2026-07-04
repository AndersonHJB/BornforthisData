var i = 0; // Start point
var images = [];
var time = 4000; /* try changing the speed and see how this changes the affect */

// This is our image List

images[0] = 'images/plugs/Chongqing.jpeg';
images[1] = 'images/plugs/Chongqing2.jpeg';
images[2] = 'images/plugs/03.png';
images[3] = 'images/plugs/04.png';
images[4] = 'images/plugs/05.png';




//this makes use of the 'onload' event to trigger the function as soon as the wondow loads

window.onload = changeImg;

// This is the function that changes the image attribute if the image tag

function changeImg() {

    //what's inside these brackets is a 'statement'

    document.slide.src = images[i];

    if (i < images.length - 1) {
        i++;
    } else {
        i = 0;
    }

    setTimeout("changeImg()", time);
}


//this function makes use of the 'onclick' event, added to our <button> html tags, to play audio

function playAudio() {

    var Audio = document.getElementById("Audio");
    if (Audio.paused) {
        Audio.play();
    } else {
        Audio.pause();
    }
}

function playAudio2() {

    var Audio = document.getElementById("Audio1");
    if (Audio.paused) {
        Audio.play();
    } else {
        Audio.pause();
    }
}

function playAudio3() {

    var Audio = document.getElementById("Audio2");
    if (Audio.paused) {
        Audio.play();
    } else {
        Audio.pause();
    }
}

//this function makes use of the 'onclick' event, also added to our <body> html tag, to open a pop up window

function mypopup() {
    mywindow = window.open("Popup1.html", "mywindow", "location=1,status=1,scrollbars=1,  width=600,height=700");
    mywindow.moveTo(0, 0);
}