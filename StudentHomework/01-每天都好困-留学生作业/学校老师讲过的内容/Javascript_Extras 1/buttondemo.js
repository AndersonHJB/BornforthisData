function myExternalFunction() {
 document.getElementById("demo3").style.textDecoration = "line-through";
}



//my calculator 

function myCalculator(a, b, c) {
                        return a + b + c;
                    }
            
var result = myCalculator(10, 20, 100);
var anotherresult = myCalculator(5000, 10000, 1000);


function calculate() {
    document.getElementById('calculator').innerHTML = result
}

function calculate2() {
    document.getElementById('calculator2').innerHTML = anotherresult
}


/*change colour of events div*/

function change() {
       
document.getElementById("events").style.backgroundColor = "#9B90C2";
document.getElementById("statements").style.backgroundColor = "#9B90C2";
}

function changeback() {
       
document.getElementById("events").style.backgroundColor = "#ffffff"; document.getElementById("statements").style.backgroundColor = "#ffffff";
    
}

/*random colour generator*/

function changeColor(){
        var color = "rgb(" + Math.floor(Math.random() * 256) + "," + 
        Math.floor(Math.random() * 256) + "," +  Math.floor(Math.random() * 256) + ")";
        document.getElementById("name").innerHTML = color;
        document.getElementById("bg").style.backgroundColor = color;
    
          }


/*return random array items*/


function getRandomArrayElement(arr){
    //Minimum value is set to 0 because array indexes start at 0.
    var min = 0;
    //Get the maximum value my getting the size of the
    //array and subtracting by 1.
    var max = (arr.length - 1);
    //Get a random integer between the min and max value.
    var randIndex = Math.floor(Math.random() * (max - min)) + min;
    //Return random value.
    return arr[randIndex];
}
 
//Example JavaScript array containing various types of animals.
var exampleArray = new Array(
    'Dog',
    'Cat',
    'Horse',
    'Penguin',
    'Lion',
    'Tiger',
    'Zebra'
);
 
//Get a random value from our array.


function randomWord(){
    var animal = getRandomArrayElement(exampleArray);
    document.getElementById("word").innerHTML = animal;
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



/*change style by seconds*/


var myVar1 = setInterval(myTimer, 1000);



/*this function returns the clock*/
function myTimer() {
  var d = new Date();
  document.getElementById("time").innerHTML = d.toLocaleTimeString();
}


/*this function changes the colour*/
var myVar2 = setInterval(colourTime, 1000);

function colourTime() {
  var time = new Date().getSeconds();
  if (time <=20 && time >=0) {   document.getElementById("timecolour").style.backgroundColor = "#9B90C2";
  }
    else if (time <=40 && time >=21) {   document.getElementById("timecolour").style.backgroundColor = "#D0104C";
  }
    else if (time <=60 && time >=41) {   document.getElementById("timecolour").style.backgroundColor = "#FC9F4D";
  }
    else {}   
}


/*this function changes the colours every 1 second*/

var myVar3 = setInterval(randomise, 1000);

function randomise(){
        var colour = "rgb(" + Math.floor(Math.random() * 256) + "," + 
        Math.floor(Math.random() * 256) + "," +  Math.floor(Math.random() * 256) + ")";      document.getElementById("automation").style.backgroundColor = colour;
 
          }

function StopColour() {
  clearInterval(myVar3);
}


/*this function changes the height every 1 second*/

var myVar4 = setInterval(quadrilateral, 100);

function quadrilateral(){
        var quadheight = Math.floor(Math.random() * 50) + "px";      document.getElementById("randomHeight").style.height = quadheight;
 
          }

function StopHeight() {
  clearInterval(myVar4);
}



//Modal

// When the user clicks the button, open the modal 
function openModal () {
      
    document.getElementById("modal").style.display =  "block";
       
}

// When the user clicks on <span> (x), close the modal
function closeModal () {
document.getElementById("modal").style.display = "none";
}


// Get the modal
var modal = document.getElementById("modal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementById("close")[0];

//pop up
function popUps() {
  window.open(document.URL, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
}


