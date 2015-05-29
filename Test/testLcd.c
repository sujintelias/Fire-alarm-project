#include"lcd.h"
void main()
{
	lcd_init();
	lcd_strwrite("Testing");
	//lcd_datawrite('c');
	while(1);
}