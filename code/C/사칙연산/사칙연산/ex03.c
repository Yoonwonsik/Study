#include <stdio.h>




int main()
{
	for (;;)
	{
		int A; // 설탕키로수
		printf("설탕 키로수를 입력하세요 :");
		scanf("%d", &A);
		int five = A / 5; // 5로 나눈값
		if (A < 0)
			break;
		if (A > 0)
		{
			for (; five >= 0;)
			{
				if ((A % 5) % 3 != 0)
				{

				}
				five = five - 1;
			}
			printf("5키로 : %d\n", five);
			printf("3키로 : %d\n", ((A % 5) / 3));
			printf("합계 : %d\n", five + ((A % 5) / 3));
		}
	}
	return 0;
}
