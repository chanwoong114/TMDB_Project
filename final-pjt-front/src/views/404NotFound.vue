<template>
  <div class="bg-gray">
    <main class="page-wrapper">
      <!-- Page content-->
      <div class="container overflow-hidden pb-5">
        <!-- Dangling lamp-->
        <div class="d-flex justify-content-center px-5 mt-n1"><img class="d-dark-mode-none" src="assets/img/404/lamp-light.png" width="348" alt="Lamp" style="transform-origin: 50% 0; animation: swinging 3.5s ease-in-out forwards infinite;"><img class="d-none d-dark-mode-block" src="assets/img/404/lamp-dark.png" width="348" alt="Lamp" style="transform-origin: 50% 0; animation: swinging 3.5s ease-in-out forwards infinite;"></div>
        <!-- Text + search bar-->
        <div class="d-flex justify-content-center pb-5 mb-md-2 mb-lg-3 mb-xl-4 mb-xxl-5">
          <div style="max-width: 420px;">
            <div class="d-none d-sm-block" style="margin-top: -127px;"></div>
            <div class="d-sm-none" style="margin-top: -25%;"></div>
            <div class="d-flex align-items-center mb-4">
              <h1 class="display-1 mb-0">404</h1>
              <p class="text-dark lead ps-4 mb-0">Whoops! That page is missing...</p>
            </div>
            
          </div>
        </div>
        <!-- Categories-->
        <h2 class="h4 text-center pb-lg-2 mb-4">Let's GAME!</h2>
        <div class="row g-4 pb-3 pb-lg-4 pb-xl-5">
          <div class="col-md-6" data-fancybox  data-src="#brick">
            <!-- Card-->
            <div class="card zoom-effect h-50 border-0 rounded-1 overflow-hidden" style="min-height: 320px;">
              <span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-10 zindex-2"></span>
              <div class="zoom-effect-wrapper rounded-1 position-absolute top-0 start-0 w-100 h-100">
                <div class="zoom-effect-img bg-size-cover bg-position-bottom-center position-absolute top-0 start-0 w-100 h-100" style="background-image: url(assets/img/404/brick.jpg);"></div>
              </div>
            </div>
          </div>
          <div id="brick" style="display:none;width:70%; height: 80%;">
            <canvas class="pt-5" id="myCanvas" width="480" height="320"></canvas>
            <br>
            <div class="d-flex justify-content-between" style="width: 30%;">
              <button class="btn btn-success" style="width: 30%;"  @click="brickgamestart">게임 시작</button>
              <button class="btn btn-danger" style="width: 30%;" @click="brickgameEnd" >게임 끝!</button>

            </div>
          </div>
          <div class="col-md-6" data-fancybox  data-src="#twozero">
            <!-- Card-->
            <div class="card zoom-effect h-50 border-0 rounded-1 overflow-hidden" style="min-height: 320px;"><span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-10 zindex-2"></span>
              <div class="zoom-effect-wrapper rounded-1 position-absolute top-0 start-0 w-100 h-100">
                <div class="zoom-effect-img bg-size-cover bg-position-bottom-center position-absolute top-0 start-0 w-100 h-100" style="background-image: url(assets/img/404/snake.png);"></div>
              </div>
            </div>
          </div>
          <div id="twozero" style="display:none;width:70%; height: 80%;">
            <canvas id="game" width="400" height="400"></canvas>
            <br>
            <div class="d-flex justify-content-between" style="width: 30%;">
              <button class="btn btn-success" style="width: 30%;"  @click="gameStart">게임 시작</button>
              <button class="btn btn-danger" style="width: 30%;" @click="gameEnd" >게임 끝!</button>

            </div>

          </div>
        </div>
      </div>
    </main>
    
  </div>
</template>

<script>

export default {
  name:"404NotFound",
  methods: {
    gameEnd() {
      this.$router.go(this.$router.currentRoute)
    },
    gameStart() {
      const canvas=document.getElementById('game');
      const ctx=canvas.getContext('2d');
      //increase snake size 
      class snakePart{
      constructor(x, y){
          this.x=x;
          this.y=y;
      }

      }

      let speed=7;
      let tileCount=20; 

      let tileSize=canvas.clientWidth/tileCount-2;
      let headX=10;
      let headY=10;

      // array for snake parts
      const snakeParts=[];
      let tailLength=2;

      //initialize the speed of snake
      let xvelocity=0;
      let yvelocity=0;

      //draw apple
      let appleX=5;
      let appleY=5;

      //scores
      let score=0;

      // create game loop-to continously update screen
      function drawGame(){
          changeSnakePosition();
          // game over logic
          let result=isGameOver();
          if(result){// if result is true
              return;
          }
          clearScreen();
          drawSnake();
          drawApple();
        
          checkCollision()
          drawScore();
          setTimeout(drawGame, 1000/speed);//update screen 7 times a second
      }
      //Game Over function
      function isGameOver(){
          let gameOver=false; 
          //check whether game has started
          if(yvelocity===0 && xvelocity===0){
              return false;
          }
          if(headX<0){//if snake hits left wall
              gameOver=true;
          }
          else if(headX===tileCount){//if snake hits right wall
              gameOver=true;
          }
          else if(headY<0){//if snake hits wall at the top
              gameOver=true;
          }
          else if(headY===tileCount){//if snake hits wall at the bottom
              gameOver=true;
          }

          //stop game when snake crush to its own body

          for(let i=0; i<snakeParts.length;i++){
              let part=snakeParts[i];
              if(part.x===headX && part.y===headY){//check whether any part of snake is occupying the same space
                  gameOver=true;
                  break; // to break out of for loop
              }
          }
          

          //display text Game Over
          if(gameOver){
          ctx.fillStyle="white";
          ctx.font="50px verdana";
          ctx.fillText("Game Over! ", canvas.clientWidth/6.5, canvas.clientHeight/2);//position our text in center
          }

          return gameOver;// this will stop execution of drawgame method
      }

      // score function
      function drawScore(){
      ctx.fillStyle="white"// set our text color to white
      ctx.font="10px verdena"//set font size to 10px of font family verdena
      ctx.fillText("Score: " +score, canvas.clientWidth-50,10);// position our score at right hand corner 

      }

      // clear our screen
      function clearScreen(){

      ctx.fillStyle= 'black'// make screen black
      ctx.fillRect(0,0,canvas.clientWidth,canvas.clientHeight)// black color start from 0px left, right to canvas width and canvas height

      }
      function drawSnake(){
          
          ctx.fillStyle="green";
          //loop through our snakeparts array
          for(let i=0;i<snakeParts.length;i++){
              //draw snake parts
              let part=snakeParts[i]
              ctx.fillRect(part.x *tileCount, part.y *tileCount, tileSize,tileSize)
          }
          //add parts to snake --through push
          snakeParts.push(new snakePart(headX,headY));//put item at the end of list next to the head
          if(snakeParts.length>tailLength){
              snakeParts.shift();//remove furthest item from  snake part if we have more than our tail size

          }
          ctx.fillStyle="orange";
          ctx.fillRect(headX* tileCount,headY* tileCount, tileSize,tileSize)


      }
      function changeSnakePosition(){
          headX=headX + xvelocity;
          headY=headY+ yvelocity;
          
      }
      function drawApple(){
          ctx.fillStyle="red";
          ctx.fillRect(appleX*tileCount, appleY*tileCount, tileSize, tileSize)
      }
      // check for collision and change apple position
      function checkCollision(){
          if(appleX==headX && appleY==headY){
              appleX=Math.floor(Math.random()*tileCount);
              appleY=Math.floor(Math.random()*tileCount);
              tailLength++;
              score++; //increase our score value

          }
      }
      //add event listener to our body
      document.body.addEventListener('keydown', keyDown);

      function keyDown()
      //up
      {
          if(event.keyCode==38){
              //prevent snake from moving in opposite direcction
              if(yvelocity==1)
              return;
              yvelocity=-1;
              xvelocity=0;
              
          }
          //down
          if(event.keyCode==40){
              if(yvelocity==-1)
              return;
              yvelocity=1;
              xvelocity=0;
          }

      //left
          if(event.keyCode==37){
              if(xvelocity==1)
              return;
              yvelocity=0;
              xvelocity=-1;
          }
          //right
          if(event.keyCode==39){
              if(xvelocity==-1)
              return;
              yvelocity=0;
              xvelocity=1;
          }
      }

      drawGame();

    },
    brickgamestart() {
      var canvas = document.getElementById("myCanvas");
      var ctx = canvas.getContext("2d");
      var ballRadius = 10;
      var x = canvas.width/2;
      var y = canvas.height-30;
      var dx = 2;
      var dy = -2;
      var paddleHeight = 10;
      var paddleWidth = 75;
      var paddleX = (canvas.width-paddleWidth)/2;
      var rightPressed = false;
      var leftPressed = false;
      var brickRowCount = 5;
      var brickColumnCount = 3;
      var brickWidth = 75;
      var brickHeight = 20;
      var brickPadding = 10;
      var brickOffsetTop = 30;
      var brickOffsetLeft = 30;
      var score = 0;
      var lives = 3;

      var bricks = [];
      for(var c=0; c<brickColumnCount; c++) {
        bricks[c] = [];
        for(var r=0; r<brickRowCount; r++) {
          bricks[c][r] = { x: 0, y: 0, status: 1 };
        }
      }

      document.addEventListener("keydown", keyDownHandler, false);
      document.addEventListener("keyup", keyUpHandler, false);
      document.addEventListener("mousemove", mouseMoveHandler, false);

      function keyDownHandler(e) {
          if(e.key == "Right" || e.key == "ArrowRight") {
              rightPressed = true;
          }
          else if(e.key == "Left" || e.key == "ArrowLeft") {
              leftPressed = true;
          }
      }

      function keyUpHandler(e) {
          if(e.key == "Right" || e.key == "ArrowRight") {
              rightPressed = false;
          }
          else if(e.key == "Left" || e.key == "ArrowLeft") {
              leftPressed = false;
          }
      }

      function mouseMoveHandler(e) {
        var relativeX = e.clientX - canvas.offsetLeft;
        if(relativeX > 0 && relativeX < canvas.width) {
          paddleX = relativeX - paddleWidth/2;
        }
      }
      function collisionDetection() {
        for(var c=0; c<brickColumnCount; c++) {
          for(var r=0; r<brickRowCount; r++) {
            var b = bricks[c][r];
            if(b.status == 1) {
              if(x > b.x && x < b.x+brickWidth && y > b.y && y < b.y+brickHeight) {
                dy = -dy;
                b.status = 0;
                score++;
                if(score == brickRowCount*brickColumnCount) {
                  alert("YOU WIN, CONGRATS!");
                  document.location.reload();
                }
              }
            }
          }
        }
      }

      function drawBall() {
        ctx.beginPath();
        ctx.arc(x, y, ballRadius, 0, Math.PI*2);
        ctx.fillStyle = "#0095DD";
        ctx.fill();
        ctx.closePath();
      }
      function drawPaddle() {
        ctx.beginPath();
        ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);
        ctx.fillStyle = "#0095DD";
        ctx.fill();
        ctx.closePath();
      }
      function drawBricks() {
        for(var c=0; c<brickColumnCount; c++) {
          for(var r=0; r<brickRowCount; r++) {
            if(bricks[c][r].status == 1) {
              var brickX = (r*(brickWidth+brickPadding))+brickOffsetLeft;
              var brickY = (c*(brickHeight+brickPadding))+brickOffsetTop;
              bricks[c][r].x = brickX;
              bricks[c][r].y = brickY;
              ctx.beginPath();
              ctx.rect(brickX, brickY, brickWidth, brickHeight);
              ctx.fillStyle = "#0095DD";
              ctx.fill();
              ctx.closePath();
            }
          }
        }
      }
      function drawScore() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Score: "+score, 8, 20);
      }
      function drawLives() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Lives: "+lives, canvas.width-65, 20);
      }

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawBricks();
        drawBall();
        drawPaddle();
        drawScore();
        drawLives();
        collisionDetection();

        if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
          dx = -dx;
        }
        if(y + dy < ballRadius) {
          dy = -dy;
        }
        else if(y + dy > canvas.height-ballRadius) {
          if(x > paddleX && x < paddleX + paddleWidth) {
            dy = -dy;
          }
          else {
            lives--;
            if(!lives) {
              alert("GAME OVER");
              document.location.reload();
            }
            else {
              x = canvas.width/2;
              y = canvas.height-30;
              dx = 3;
              dy = -3;
              paddleX = (canvas.width-paddleWidth)/2;
            }
          }
        }

        if(rightPressed && paddleX < canvas.width-paddleWidth) {
          paddleX += 7;
        }
        else if(leftPressed && paddleX > 0) {
          paddleX -= 7;
        }

        x += dx;
        y += dy;
        requestAnimationFrame(draw);
      }

      draw();
    },
    brickgameEnd() {
      this.$router.go(this.$router.currentRoute)
    }
  },
}
</script>

<style scoped>
  * { padding: 0; margin: 0; }
  canvas { background: #eee; display: block; margin: 0 auto; }

  #brick {
    display: flex;
    flex-direction: column; /* arrage items on top of the other */
    justify-content: center;
    align-items: center;
  }

  #twozero{
  margin: 0px;
  padding: 0px;
  display: flex;
  flex-direction: column; /* arrage items on top of the other */
  justify-content: center;
  align-items: center;
  }
  canvas{
  border: 1px solid black; /*elevate our canvas and add shadow*/

  }
</style>