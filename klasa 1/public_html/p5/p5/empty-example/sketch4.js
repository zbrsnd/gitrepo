var x, y;  //współrzędne obiektu

x = y = 100;
function setup() {
  // put setup code here
  createCanvas(600, 600);


}

function draw() {
  
    
  background(200);
  dx = mouseX - x
  dy = mouseY - y
  angle1 = atan2(dy, dx);
  x = mouseX - (cos(angle1) * 30);
  y = mouseY - (sin(angle1) * 30);
    
    fill('yellow');
    rect(x, y, 70, 70);
     

}