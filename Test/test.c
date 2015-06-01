 #include<reg51.h>
 #include"delay.h"
 #define led1 P0
 #define led2 P1
 
 void main()
 {
   led1=0xaa;
   led2=0x55;
   delay_sec(1);
   led1=0x00;
   led2=0x00;
   delay_sec(1);
 
 }