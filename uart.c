#include<reg51.h>
void uart_init()
{
	TMOD |=0x20; //Timer1 in Mode2.
	TH1=-3;    // 9600 Baud rate at 11.0592MHz
	SCON=0x50; // Asynchronous mode 8-bit data and 1-stop bit
	TR1 = 1;	 //Turn ON the timer.
	RI=0;
}

void uart_txchar(char ch)
{
	SBUF=ch;	   // Load the data to be transmitted
  	while(TI==0);    // Wait till the data is trasmitted
    TI=0;
}
char uart_rxchar()
{
	while(RI==0);	  // Wait till the data is received
    RI=0;        // Clear Receive Interrupt Flag for next cycle
  	return(SBUF);	  // return the received char
}
void uart_txstring(unsigned char ch[100])
 {
	int x;
	
 	for(x=0;ch[x]!='\0';x++)
		uart_txchar (ch[x]);
	uart_txchar('\n');
	while(1);
 }