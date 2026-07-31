
//This function swaps out the heading for this new text

function changeHeading() {


    document.getElementById('heading1').innerHTML = "Lets get this done";


}

function changeHeading2() {


    document.getElementById('heading2').innerHTML = "HERE WE GO AGAIN";


}


//This function changes the 'background' css property for the div #background

function changeBackground() {

    document.getElementById("background").style.background = "linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1))";
    document.getElementById("background2").style.background = "linear-gradient(to right, red , blue)";


}


//These functions play audio and video - you will need these and you may implement them in your work 

function playAudio() {

    var Audio = document.getElementById("Audio");
    if (Audio.paused) {
        Audio.play();
        Audio.volume = 1;
    } else {
        Audio.pause();
    }
}


function playAudio2() {

    var Audio = document.getElementById("Audio2");

    if (Audio.paused) {
        Audio.play();
        Audio.volume = 0.4;
    } else {
        Audio.pause();
    }
}


function playVid() {

    let vid = document.getElementById("myVideo");

    if (vid.paused) {
        vid.play();

    } else {
        vid.pause();
    }
}





//This function opens a pop up window, think about how you could use this in your work - perhaps your whole world is a series of popups.. 


function mypopup() {
    mywindow = window.open("popup.html", "mywindow", "location=1,status=1,scrollbars=1,  width=600,height=700");
    mywindow.moveTo(0, 0);
}


function mypopup2() {
    mywindow2 = window.open("popup2.html", "mywindow2", "location=1,status=1,scrollbars=1,  width=1400,height=60");
    mywindow2.moveTo(0, 0);
}


/*trigger sound*/


document.addEventListener('keydown', function(e) {
  if (e.keyCode == 32) {
    document.getElementById('audio').play();    
  }
});
document.addEventListener('keyup', function(e) {
  if (e.keyCode == 32) {
    document.getElementById('audio1').play();    
  }
});

document.addEventListener('keydown', function(e) {
  if (e.keyCode == 13) {
    document.getElementById('audio1').play();
  }
});
document.addEventListener('keydown', function(e) {
  if (e.keyCode == 81) {
    document.getElementById('audio2').play();
  }
});
document.addEventListener('keydown', function(e) {
  if (e.keyCode == 87) {
    document.getElementById('audio3').play();
  }
});
document.addEventListener('keydown', function(e) {
  if (e.keyCode == 69) {
    document.getElementById('audio4').play();
  }
});

//Notice that in this function we are creating a 'variable' in the form of a video element and a text node - we use variables when we need to create an object in the computer's memory which we will then assign values to, ie play, width, height etc - our play audio and video functions work in the same way. Note 'var' and 'let' do the same thing


function createVideo() {

    //this part of the function creates our elements - note we are also creating a new div element which appears below

    var x = document.createElement("video");
    let t = document.createTextNode("Here we have created a new video, 2 x audio elements and a text node, and appended them to our span element. We have also created a new div element, which we have appended to the body, and a button, which we have appended to the new div. The button has an 'onclick' event listener which calls a function that changes the background of the new div.");
    var a = document.createElement("audio");
    var d = document.createElement("div");
    var b = document.createElement("button");
    b.textContent = 'Another Function';


    //this part sets attributes and parameters for our elements

    x.src = "video/train2.mp4"
    a.src = 'sound/ambience.mp3';
    x.muted = false;
    x.loop = true;
    x.setAttribute("style", "opacity:0.8;");
    d.setAttribute("class", "aClassName container");
    d.setAttribute("id", "newDiv");
    b.addEventListener("click", newFunction);
    

    //this part plays the audio i.e. the variable 'a'

    if (a.paused) {
        a.play();
        a.volume = 1;
    } else {
        a.pause();
    }

    

     //this part plays the video i.e. the variable 'x'

     if (x.paused) {
        x.play();
        x.volume = 0.3;
        
    } else {
        x.pause();
    }

    

    //this part appends the new elements to #VideoContainer, except the new div, which appended to the body, and the button, which is appended to the new div


    document.getElementById("VideoContainer").appendChild(x);
    document.getElementById("VideoContainer").appendChild(t);
    document.getElementById("VideoContainer").appendChild(a);
    document.body.appendChild(d);
    document.getElementById("newDiv").appendChild(b);
    


}


  //HINT: You must define this function before you can use it in the event listener above, so it must be defined before the createVideo function is called.

 function newFunction() {

document.getElementById('newDiv').style.background = "linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1))";

 }

