#include <reg51.h>
#include "delay.h"
#include "uart.h"
#define segs P1
#define datas P0
sbit bzr=P2^0;
void fire(unsigned char str[4])
{
	
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
	   unsigned char fireCode[]={0x8e,0x0c,0xee,0x9e};
	   unsigned char initCode[]={0x01,0x01,0x01,0x01};

	   char msg;
	   uart_init();
	         
     	msg=uart_rxchar();
	
 	
	  
		while(1)
		{
	    msg=uart_rxchar();  
	    
		if(msg=='f')
			{
			    uart_txchar('f');
	      	    bzr=1;
				for(i=0;i<200;i++)
				fire(fireCode); 
				bzr=0;
				delay_sec(1);				 
		  	 }
 	       	else if(msg=='q')
			 {
		        uart_txchar('O');
				segs=0x00;
				bzr=0;
		 	 }
			else 
			 {
			   uart_txchar('O');
			   bzr=0;
			   fire(initCode);

			 } 	 
								
		 }
					
	
}		  	 
	
