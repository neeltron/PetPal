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
  S1.write(90);
  delay(1000);
  S1.write(0);
  delay(1000);
}
