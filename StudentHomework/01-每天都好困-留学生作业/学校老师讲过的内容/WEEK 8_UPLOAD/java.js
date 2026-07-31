var currentpic = 0;
var currentsentence = 0;
var currentpic2 = 0;
var currentsentence2 = 0;


function nextslide() {
    var images = new Array()
    images[0] = 'images/01.png';
    images[1] = 'images/02.png';
    images[2] = 'images/03.png';
    images[3] = 'images/04.png';
    images[4] = 'images/05.png';
    images[5] = 'images/06.png';
    images[6] = 'images/07.png';
    images[7] = 'images/08.png';
    images[8] = 'images/09.png';
    images[9] = 'images/10.png';


    var lastpic = images.length - 1;
    if (currentpic == lastpic) {
        currentpic = 0;
        document.getElementById('slide').src = images[currentpic];
    } else {
        currentpic++;
        document.getElementById('slide').src = images[currentpic];
    }
}


function nextsubtitle() {
    var words = new Array()

    words[0] = "CHAPTER 1";
    words[1] = "Here is some more text continuing my narrative";
    words[2] = "Here is different text continuing my narrative";
    words[3] = "Read another exciting installment ";
    words[4] = "And then...";
    words[5] = "More interesting things happened";
    words[6] = "The future was shocking, but comforting somehow";
    words[7] = "But things weren't exactly as they seemed";
    words[8] = "Here is some more text continuing my narrative";
    words[9] = "Perhaps at this point we might move on to another page";

    var lastwords = words.length - 1;
    if (currentsentence == lastwords) {
        currentsentence = 0;
        document.getElementById('text1').innerHTML = words[currentsentence];
    } else {
        currentsentence++;
        document.getElementById('text1').innerHTML = words[currentsentence];
    }
}







function playAudio() {

    var Audio = document.getElementById("Audio");
    if (Audio.paused) {
        Audio.play();
    } else {
        Audio.pause();
    }
}



function playAudio2() {

    var Audio = document.getElementById("Audio2");

    if (Audio.paused) {
        Audio.play();
        Audio.volume = 0.1;
    } else {
        Audio.pause();
    }
}


function playVid() {

    let vid = document.getElementById("video1");

    if (vid.paused) {
        vid.play();

    } else {
        vid.pause();
    }
}

function disappear() {

    document.getElementById("text2").style.opacity = "0";

}


function videoload() {

    mywindow = window.open("Popup1.html", "mywindow", "location=1,status=1,scrollbars=1,  width=800,height=500");
    mywindow.moveTo(0, 0);

    document.getElementById("text2").style.opacity = "1";
    document.getElementById("text2").innerHTML = "scroll down";


    document.getElementById("video1").src = "video/rig.mp4";
    var x = document.getElementById("video1");
    x.autoplay = true;
}

