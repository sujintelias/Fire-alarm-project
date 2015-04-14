#include <reg51.h>
#include "delay.h"
#include "uart.h"
#define segs P1
#define datas P0
void fire()
{
	unsigned char str[]={0x8e,0x0c,0xee,0x9e};
	datas=str[0];
    segs=0x18;
	delay_us(250);
	datas=str[1];
	segs=0x14;
	delay_us(250);	
	datas=str[2];
	segs=0x12;
	delay_us(250);		  
	datas=str[3];
	segs=0x11;
	delay_us(250);
	segs=0x00;
	delay_us(250);

}


void main()
	{	
		int i;
		char msg;
		uart_init();
		msg=uart_rxchar();
	 	while (msg=='f')
		  {
		   
		   	for(i=0;i<200;i++)
					fire();
			
				delay_sec(1);
		   				
		  
		  if(msg=='o')
		  {
		  	segs=0x00;
		  }

		  }            //edited cmnt
	}
	   	
		  	 
	
