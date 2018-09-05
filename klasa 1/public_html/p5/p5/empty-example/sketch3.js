var x, y;  //współrzędne obiektu
var krok = -1;
function setup() {
  // put setup code here
  createCanvas(600, 600);
  background(200);
  x = 575;
  y = 475;

}

function draw() {

  noFill();
  noStroke();
  if (mouseIsPressed) {
    if (mouseButton === LEFT) {  // SPRAWDZANIE KTÓRY PRZYCISK MYSZY JEST NACIŚNIĘTY " === "
      fill('red');
      strokeWeight(30);
      stroke(random(255));
    }
    if (mouseButton === CENTER) {
      strokeWeight(20);
      fill(200);
      rect(mouseX-10, mouseY-10, 30, 30);   //GUMKA W KSZTALCIE KWADRATU
    }

 }
 point(mouseX, mouseY);
}
