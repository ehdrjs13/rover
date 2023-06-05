#include <Servo.h>

const int servoPin = 7; 
Servo servo;

const int dcpin1 = 8;
const int dcpin2 = 9; //ena핀은 스팀 작품에서 dc 속도조절이 굳이 필요하지 않을 것 같아 제외했습니다.

char input = 0;

void setup() {
  Serial.begin(9600);


  servo.attach(servoPin);
  pinMode(dcpin1, OUTPUT);
  pinMode(dcpin2, OUTPUT);
}

//상하좌우 제어 함수들 선언
void forward() {
  servo.write(90);
  digitalWrite(dcpin1, HIGH);
  digitalWrite(dcpin2, LOW);
}

void backward() {
  servo.write(90);
  digitalWrite(dcpin1, LOW);
  digitalWrite(dcpin2, HIGH);
}

void left() {
  servo.write(45);
  digitalWrite(dcpin1, HIGH);
  digitalWrite(dcpin2, LOW);
}


void right() {
  servo.write(135);
  digitalWrite(dcpin1, HIGH);
  digitalWrite(dcpin2, LOW);
}


void stop() {
  servo.write(90)
  digitalWrite(dcpin1, LOW);
  digitalWrite(dcpin2, LOW);
}

//움직임 제어(위에 선언된 함수 사용)
void loop() {
  if (Serial.available() > 0) {
    input = Serial.read();
  if (input == 'w') {
    forward();
  } 
  else if (input == 's') {
    backward();
  } 
  else if (input == 'a') {
    left();
  } 
  else if (input == 'd') {
    right();
  } 
  else {
    stop();
   }
 }
}


