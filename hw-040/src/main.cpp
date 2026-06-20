#include <Arduino.h>
#include <RotaryEncoder.h>

#define PIN_CLK 2
#define PIN_DT  3
#define PIN_SW  4

RotaryEncoder encoder(PIN_CLK, PIN_DT, RotaryEncoder::LatchMode::FOUR3);

long lastPosition = 0;
int lastButtonState = HIGH;

void printState(long position, int buttonState) {
  int buttonPressed = (buttonState == LOW) ? 1 : 0;

  Serial.print(position);
  Serial.print(",");
  Serial.println(buttonPressed);
}

void setup() {
  Serial.begin(9600);

  pinMode(PIN_CLK, INPUT_PULLUP);
  pinMode(PIN_DT, INPUT_PULLUP);
  pinMode(PIN_SW, INPUT_PULLUP);

  lastPosition = encoder.getPosition();
  lastButtonState = digitalRead(PIN_SW);

  Serial.println("position,button");
  printState(lastPosition, lastButtonState);
}

void loop() {
  encoder.tick();

  long position = encoder.getPosition();
  int buttonState = digitalRead(PIN_SW);

  if (position != lastPosition || buttonState != lastButtonState) {
    printState(position, buttonState);

    lastPosition = position;
    lastButtonState = buttonState;
  }
}