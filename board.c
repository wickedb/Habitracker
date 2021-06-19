/*Code for Arduino Uno.
Displays text on LCD and listens for the push button status.*/

#include <LiquidCrystal.h>

const int button = 9;   
const int led =  8;  
int buttonStatus = 0;  

LiquidCrystal lcd(12,11,5,4,3,2);

void setup() {
  
  lcd.begin(16, 2);
  lcd.print("Reminder!!");
   pinMode(led,HIGH);
  pinMode(button,LOW);
  Serial.begin(9600);
  
}

void loop() {
  lcd.setCursor(1, 1);
  lcd.print("Done?");
   buttonStatus = digitalRead(button);
  if (buttonStatus == HIGH) {    
    digitalWrite(led, HIGH);
  }
  else {   
    digitalWrite(led, LOW);
  }
  Serial.println(buttonStatus);
  
}
