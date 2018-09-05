var x, y;  //współrzędne obiektu
var krok = -1
function setup() {
  // put setup code here
  createCanvas(600, 600);
  x = 575;
  y = 475;

}

function draw() {
  // put drawing code here
  background(200);
  r = random(255);
  g = random(255);
  b = random(255);
  //x = random(685);
  //y = random(685);

  fill(r, g, b);
  strokeWeight(1);
  stroke('black');

  if (x > 14) { // <--- środek koła ma współrzędne 15,15 [30/2], stąd większe od 14 zeby szedl wzdluz krawedzi canvasu
    x = x + krok;
  } else {
    x = x - krok
  }
  if (y > 14) {
    y = y - krok
  } else {
    y = y - krok
  }

  ellipse(x, y, 30, 30);
  ellipse(x+50, y+50, 30, 30);
  ellipse(x+100, y, 30, 30);
  ellipse(x+150, y+50, 30, 30);

  //  ellipse(x, y, szerokosc, wysokosc)
}
