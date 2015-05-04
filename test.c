#include <reg51.h>
#include "delay.h"
#include "uart.h"
void main()
{
	uart_init();
	while(1)
	{
		   uart_txchar('f');
		   //delay_sec(1);
	}
}