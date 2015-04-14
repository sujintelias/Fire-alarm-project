#include<reg51.h>
void uart_init()
{
	SCON = 0x50; // Cofigure UART
	TMOD = 0x20;
	TH1 = -3;
	TR1 = 1;
			
}

void uart_txchar(char ch)
{
	SBUF = ch;
	while(TI == 0);
	TI = 0;
}
char uart_rxchar()
	{
	while(RI==0);
	RI=0;
	return SBUF;
	}
void uart_txstring(unsigned char ch[100])
 {
	int x;
	
 	for(x=0;ch[x]!='\0';x++)
		uart_txchar (ch[x]);
	uart_txchar('\n');
	while(1);
 }