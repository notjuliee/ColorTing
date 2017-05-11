int redPin = 9;
int greenPin = 10;
int bluePin = 11;

int redVal = 255;
int greenVal = 0;
int blueVal = 255;

String str;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0) {
    redVal = Serial.parseInt();
    greenVal = Serial.parseInt();
    blueVal = Serial.parseInt();

    if (Serial.read() == '\n') {
      analogWrite(redPin, redVal);
      delay(30);
      analogWrite(greenPin, greenVal);
      delay(30);
      analogWrite(bluePin, blueVal);
      delay(30);

      Serial.print(redVal, HEX);
      Serial.print(greenVal, HEX);
      Serial.println(blueVal, HEX);
    }
  }
}
