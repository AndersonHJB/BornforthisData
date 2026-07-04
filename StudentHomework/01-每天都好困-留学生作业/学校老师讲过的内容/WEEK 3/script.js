function playAudio() {

    var Audio = document.getElementById("Audio");
    if (Audio.paused) {
        Audio.play();
    } else {
        Audio.pause();
    }
}


var myVar3 = setInterval(randomise, 1000);

function randomise() {
    var colour = "rgb(" + Math.floor(Math.random() * 256) + "," +
        Math.floor(Math.random() * 256) + "," + Math.floor(Math.random() * 256) + ")";
    document.getElementById("automation").style.backgroundColor = colour;

}
