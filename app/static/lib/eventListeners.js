let mouseX = 0;
let mouseY = 0;
let mouseDown = false;

document.onmousemove = function(event) {
    mouseX = event.pageX;
    mouseY = event.pageY;
}
document.onmousedown = function(event) { 
    mouseDown = true;
}
document.onmouseup = function(event) {
    mouseDown = false;
}