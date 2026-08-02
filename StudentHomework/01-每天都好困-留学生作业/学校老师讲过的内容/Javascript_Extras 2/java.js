


/*SCROLLING DESKTOP IMAGES */

window.onload = changeImg;

var i = 0; // Start point - the beginning of the 'index'
var time = 500; //speed in ms
var images = [];// empty array


// Image List - here 'images' denotes the name of the array, the number in the [] is the index number of the image, and then we have the url that points to the file.

images[0] = 'images/desktop/01.png';
images[1] = 'images/desktop/02.png';
images[2] = 'images/desktop/03.png';
images[3] = 'images/desktop/04.png';
images[4] = 'images/desktop/05.png';
images[5] = 'images/desktop/06.png';
images[6] = 'images/desktop/07.png';
images[7] = 'images/desktop/08.png';
images[8] = 'images/desktop/09.png';
images[9] = 'images/desktop/10.png';
images[10] = 'images/desktop/11.png';




// below is our function

function changeImg(){

        
        
document.getElementById("slide").setAttribute("src",images[i]); //because we have set the variable i = 0, the first image in our array will be loaded when the function is run for the first time.
    
//below is an if statement - the length of our array is 11, but the array begins at 0 so we need to subtract one from the overall length to get 10, which is the last image in the array.
    
//So, if 'i' is less than 11, the function will add 1 to the variable 'i' - this ensure the function will be executed until i = 12, at which point 'i' will revert to 0 and the process will repeat.
        
		if(i < images.length - 1){  
			i++;
		} else {
			i = 0;
		}

setTimeout("changeImg()", time); //setimeout runs the function every 450 ms
    
    
	}

/* SCROLLING SUBTITLES */

var x = 0;
var myVar2 = setInterval(words2, 400);


 function words2() { 

    var array2 = [ "CHAPTER 1","The interface serves to organize raced and gendered bodies in categories,", "boxes, and links that mimic both the mental structure", "of a normative consciousness and set of associations", "(often white, often male)","to click on a box or link is to acquire it, to choose it", "to replace one set of images with another in a friction-free transaction",  "that seems to cost nothing yet generates capital in the form of digitally racialized images and performances.", "hello here is a new line"];
     
    
     
      x = x + 1;


    document.getElementById("subs").innerHTML = array2[x];
   
     
   if (x == 9) {
       
     x = 0;
       
   }

     }




/*RANDOM IMAGES AND LINKS*/
var myImages1 = new Array();
myImages1.push("images/cursed/1.jpg");
myImages1.push("images/cursed/2.jpg");
myImages1.push("images/cursed/3.jpg");
myImages1.push("images/cursed/4.jpg");
myImages1.push("images/cursed/5.jpg");
myImages1.push("images/cursed/6.jpg");


//create a random interger between 0 and the length of the array above, the parameters correspond with the variable x in the next function

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


// this function runs the function above and uses the random integer as a value to 'push' items from the array using the getElementById method

function pickimg2() {
    
    var x = myImages1[getRandomInt(0, myImages1.length - 1)];
  
    document.randimg.src = x;
    document.getElementById("demo").innerHTML = x;
    document.getElementById("demo").setAttribute("href", x + ".html");  
}


/*RANDOM WORD GENERATOR*/


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
    'Zebra',
    'Dummy'
);
 
//Get a random value from our array, generate a text node and a paragraph element to hold it, and append div. This function also applies a class to all the generated <p> tags and applies a randomly generated number to the transform property


function randomWord(){
    
    var animal = getRandomArrayElement(exampleArray); 
    var para = document.createElement("p");
    para.classList.add("newWords");
    //para.setAttribute("id", 'animal' + counter++);
     var text = document.createTextNode(animal);    
    para.appendChild(text); 
    document.getElementById("addwords").appendChild(para);
   
    //the parameters determine which new node and element gets paired with with which variable ie random array item and new p element
           
    var value = "skewX(" + Math.floor(Math.random() * 360) + "deg)";  
    
    var list = document.getElementsByClassName('newWords');
    for(i = 1; i < list.length; i++) {list[i].style.transform = value;
  }
    
}

//this function applies an id to each of the first five paragraph tags that are generated, allowing us to style them seperately.

function changeclass () { 
    
    document.getElementsByClassName("newWords")[1].setAttribute("id", "animal1");
    document.getElementsByClassName("newWords")[2].setAttribute("id", "animal2");
    document.getElementsByClassName("newWords")[3].setAttribute("id", "animal3");
    document.getElementsByClassName("newWords")[4].setAttribute("id", "animal4");
    document.getElementsByClassName("newWords")[5].setAttribute("id", "animal5");

}





/*IMAGE MODAL*/


/*modal script*/

function openModal() {
  document.getElementById("myModal").style.display = "block";
}

function closeModal() {
  document.getElementById("myModal").style.display = "none";
}






var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}


title = "Your Title";
position = 0;
function scrolltitle() {
    document.title = title.substring(position, title.length) + title.substring(0, position); 
    position++;
    if (position > title.length) position = 0;
    titleScroll = window.setTimeout(scrolltitle,170);
}
scrolltitle();








	




