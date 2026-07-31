//event listener adds a class for my text animation at the bottom of my html

document.addEventListener('DOMContentLoaded', function() {
    const starWarsText = document.getElementById('star-wars-text');

    starWarsText.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default behavior if it's a link
        this.classList.toggle('animate');
    });
});

//This function opens a pop up window, think about how you could use this in your work - perhaps your whole world is a series of popups.. 


function mypopup() {
    mywindow = window.open("popup.html", "mywindow", "location=1,status=1,scrollbars=1,  width=600,height=700");
    mywindow.moveTo(0, 0);
}


function mypopup2() {
    mywindow2 = window.open("popup2.html", "mywindow2", "location=1,status=1,scrollbars=1,  width=1400,height=60");
    mywindow2.moveTo(0, 0);
}


//this function creates our elements. Notice that in this function we are creating a 'variable' in the form of a video element and a text node - we use variables when we need to create an object in the computer's memory which we will then assign values to, ie play, width, height etc - our play audio and video functions work in the same way. Note 'var' and 'let' do the same thing


function createVideo() {

    //this part of the function creates our elements - note we are also creating a new div element which appears below

    var x = document.createElement("video");
    let t = document.createTextNode("Here we have created a new video, 2 x audio elements and a text node, and appended them to our span element. We have also created a new div element, which we have appended to the body, and a button, which we have appended to the new div. The button has an 'onclick' event listener which calls a function that changes the background of the new div.");
    var a = document.createElement("audio");



    //this part sets attributes and parameters for our elements

    x.src = "video/train2.mp4"
    a.src = 'sound/ambience.mp3';
    x.muted = false;
    x.loop = true;
  

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

}





/*SCROLLING DESKTOP IMAGES */



//window.onload = changeImg; 
//(we could begin the slideshow upon load)

var i = 1; // Start point - the beginning of the 'index'
var time = 2000; //speed in ms
var images = [];// empty array


// Image List - here 'images' denotes the name of the array, the number in the [] is the index number of the image, and then we have the url that points to the file.

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





// below is our function

function changeImg(){

        
        
document.getElementById("slide1").setAttribute("src",images[i]); //because we have set the variable i = 0, the first image in our array will be loaded when the function is run for the first time.
    
//below is an if statement - the length of our array is 11, but the array begins at 0 so we need to subtract one from the overall length to get 10, which is the last image in the array.
    
//So, if 'i' is less than 11, the function will add 1 to the variable 'i' - this ensure the function will be executed until i = 12, at which point 'i' will revert to 0 and the process will repeat.
        
		if(i < images.length - 1){  
			i++;
		} else {
			destroyElements()
		}

setTimeout("changeImg()", time); //setimeout runs the function every 1000 ms
    
    
	}

    function destroyElements() {

    document.getElementById("slide1").style.opacity = "0";
    document.getElementById("text1").style.opacity = "0";
    var Audio = document.getElementById("AudioSlide1");
   Audio.pause(); 
   audio.currentTime = 0;

    }

/* SCROLLING SUBTITLES */

var x = 0;
//var myVar2 = setInterval(words, 1000);


 function words() { 

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

     
      x = x + 1;


    document.getElementById("text1").innerHTML = words[x];
   
     
   if (x == 9) {
       
     x = -1;
       
   }

   setTimeout("words()", time); //setimeout runs the function every 1000 ms

   

     }





/*ON-CLICK SCROLLING DESKTOP IMAGES */


var currentpic = 0;


function nextslide2() {
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
        document.getElementById('slide2').src = images[currentpic];
    } else {
        currentpic++;
        document.getElementById('slide2').src = images[currentpic];
    }
}

/*ON-CLICK SCROLLING TEXT */

var currentsentence = 0;

function nextsubtitle2() {
    var words2 = new Array()

    words2[0] = "CHAPTER 1";
    words2[1] = "Here is some more text continuing my narrative";
    words2[2] = "Here is different text continuing my narrative";
    words2[3] = "Read another exciting installment ";
    words2[4] = "And then...";
    words2[5] = "More interesting things happened";
    words2[6] = "The future was shocking, but comforting somehow";
    words2[7] = "But things weren't exactly as they seemed";
    words2[8] = "Here is some more text continuing my narrative";
    words2[9] = "Perhaps at this point we might move on to another page";

    var lastwords = words2.length - 1;
     

    if (currentsentence < lastwords) {
        currentsentence++;
        document.getElementById('text2').innerHTML = words2[currentsentence];
    } else {
        destroyElements2()
      
    }
 
}

 function destroyElements2() {

    document.getElementById("slide2").style.opacity = "0";
    document.getElementById("text2").style.opacity = "0";
    var Audio2 = document.getElementById("AudioSlide2");
   Audio2.pause();  
   audio2.currentTime = 0;
    }

    //This function swaps out the heading for this new text

function changeText() {


    document.getElementById('newText1').innerHTML = "This is a very simple way to create interaction by swapping out the text in a paragraph or span element.<br><br> How can you adapt this for your own project? <br><br> How could you adapt this row so that we have three columns each with a different version of this function?<br><br>How could we also change the styling on our text?";


}

//These functions play audio and video in the 2nd row - you will need these and you may implement them in your work 

function playAudioNew() {

    var Audio = document.getElementById("AudioNew");
    if (Audio.paused) {
        Audio.play();
        Audio.volume = 1;
    } else {
        Audio.pause();
    }
}


function playAudioNew2() {

    var Audio = document.getElementById("AudioNew2");

    if (Audio.paused) {
        Audio.play();
        Audio.volume = 0.4;
    } else {
        Audio.pause();
    }
}


function playVidNew() {

    let vid = document.getElementById("myVideoNew");

    if (vid.paused) {
        vid.play();

    } else {
        vid.pause();
    }
}


function playAudioSlide1() {

    var Audio = document.getElementById("AudioSlide1");
    Audio.play();
}


function playAudioSlide2() {

    var Audio2 = document.getElementById("AudioSlide2");
        Audio2.play();
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

    document.getElementById("playButton").style.opacity = "0";

}

function disappear2() {

    document.getElementById("playButton2").style.opacity = "0";

}


var mywindow; // Declare mywindow globally

function videoload() {
    mywindow = window.open("Popup1.html", "mywindow", "location=1,status=1,scrollbars=1, width=800,height=500");
    mywindow.moveTo(0, 0);

    var x = document.getElementById("video1");
    x.play();
    x.loop = true; // corrected from x.loop()
}

 mywindow.onload = function() {
        var y = mywindow.document.getElementById("videopopup");
            y.play();
            y.loop = true; // 
    };




