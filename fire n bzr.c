#include <reg51.h>
#include "delay.h"
#include "uart.h"
#include "lcd.h"
#define segs P1
#define datas P0
sbit bzr=P3^2;
sbit ack=P3^3;
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
	   char prevMsg;
	   bzr=0;
	   lcd_init();
	   lcd_clear();
	   lcd_strwrite("Init");
	   
	   uart_init();
	   //msg=uart_rxchar(); //Extra ???
		while(1)
		{	
			
		   	msg=uart_rxchar(prevMsg);
			
			
			if (msg!=prevMsg)
			{   prevMsg = msg;
				//uart_txchar(msg);   //Acknowledgement

				uart_txchar(msg); //Debug code
			}
			else
			{
			 	//uart_txchar(msg+1);   //Bug Acknowledgement
				uart_txchar(msg+1);		//Debug Code
			}

		    //uart_txchar(msg);   //Acknowledgement

			if(msg=='f')
			{   
					if(ack==0)
					{
						bzr=1;
						lcd_clear();
						lcd_strwrite("Client1");
					}
					else
					{
						bzr=0;
						lcd_clear();
						lcd_strwrite("ACK");
					}
					for(i=0;i<200;i++)
						fire(fireCode); 
					bzr=0;
					delay_sec(1);				 
		  	 }
			else 
			 {
				   bzr=0;
				   for(i=0;i<200;i++)
				   	fire(initCode);
				   lcd_clear();
	   				lcd_strwrite("Init");
			 } 	 
								
		 }	  //End of infinite loop
					
	
}		  	 
	
