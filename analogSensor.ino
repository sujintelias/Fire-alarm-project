#include <SoftwareSerial.h>
int sensor = 0;
void setup() {
Serial.begin(9600);
pinMode(sensor,INPUT);

}

void loop() 
{
  
   int val;
   val = analogRead(sensor);
   
   float mv = ( val/1024.0)*5000; 
   float cel = mv/10;

   if (cel>=40 and cel<=50)
   {
     delay(5000);
     Serial.println("f");
   }
   
}
