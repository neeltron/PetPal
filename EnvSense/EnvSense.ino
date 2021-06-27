#include<dht11.h>
dht11 DHT;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int chk = DHT.read(2);
  Serial.println(DHT.temperature);
}
