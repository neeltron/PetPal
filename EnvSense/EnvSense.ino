#include<dht11.h>
#include <Servo.h>
dht11 DHT;
Servo S1;

void setup() {
  Serial.begin(9600);
  S1.attach(3);
}

void loop() {
  int chk = DHT.read(2);
  Serial.println(DHT.temperature);
  int servo = Serial.read();
  if (servo == 65) {
    S1.write(90);
  }
  if(servo == 66) {
    S1.write(45);
  }
  if(servo == 67) {
    S1.write(135);
  }
}
