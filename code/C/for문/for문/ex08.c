#include <stdio.h>

int main()
{
	int x = 0, y = 0, daycal =0;
	printf("월, 일 입력 : ");
	scanf("%d %d", &x, &y);
	int a[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	for (int i = 1; i <= x; i = i + 1)
	{
		daycal = daycal + a[i-1];
		y = y + daycal;
	}
	int day = y % 7;

	switch (day)
	{
	case 0 :printf("SUN\n");break;
	case 1 :printf("MON\n");break;
	case 2 :printf("TUE\n");break;
	case 3 :printf("WED\n");break;
	case 4 :printf("THU\n");break;
	case 5 :printf("FRI\n");break;
	case 6 :printf("SAT\n");break;
	default:
		break;
	}

	return 0;
}