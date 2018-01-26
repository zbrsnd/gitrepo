function setup() {
  // put setup code here
  createCanvas(700, 700);
}

function draw() {
  // put drawing code here
  fill("#7c6bea");
  strokeWeight(2);
  stroke('black');
  ellipse(100, 200, 90, 40);
  fill("#7c6bea");
  strokeWeight(3);
  stroke('black');
  ellipse(50, 100, 40, 90);

  strokeWeight(5);
  stroke('black');
  line(10, 10, 60, 60);
  line(60, 10, 10, 60);

  stroke('green');
  fill('green');
  point(300,300);

  stroke('blue');
  fill('black');
  rect(100, 240, 55, 55);

  //  ellipse(x, y, szerokosc, wysokosc)
}
