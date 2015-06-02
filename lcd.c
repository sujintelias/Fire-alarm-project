#include<reg51.h>
#include "delay.h"
#define lcdd P2
sbit rs=P3^7;
sbit rw=P3^6;
sbit e=P3^5;
void lcd_cmdwrite(char cmd)
{
	lcdd=cmd;
	rs=0;
	rw=0;
	e=1;
	delay_us(10);
	e=0;
	delay_ms(1);
}




void lcd_datawrite(char dat)
{
	lcdd=dat;
	rs=1; 
	rw=0;
	e=1;
	delay_us(10);
	e=0;
	delay_ms(1);
 }

void lcd_strwrite(char s[100])
{
	int i;
	for(i=0;s[i]!='\0';i++)
		   lcd_datawrite(s[i]);
}
void lcd_init()
{
	lcd_cmdwrite(0x38);
	lcd_cmdwrite(0x0e);
	lcd_cmdwrite(0x01);
	lcd_cmdwrite(0x80);
}
void lcd_clear()
{
  	lcd_cmdwrite(0x01);
	lcd_cmdwrite(0x80);
}