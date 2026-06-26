#include <Arduino.h>

int AO = A0;
int DO = 2;

void setup() {
  Serial.begin(9600);
  Serial.println("Sound sensor ready");
  pinMode(DO, INPUT_PULLUP);
  pinMode(AO, INPUT);
}

void loop() {
  int soundLevel = analogRead(AO);
  int soundDetected = digitalRead(DO);
  if (soundDetected == LOW) {
    Serial.println("Sound detected!");
    Serial.print("Sound level: ");
    Serial.println(soundLevel);
  }
}