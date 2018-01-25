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
		else if (A > 0)
		{
			if (five == 0)
			{
				for (; five = 0;)
				{

				}
				printf("5키로 : %d\n", five);
				printf("3키로 : %d\n", ((A % 5) / 3));
				printf("합계 : %d\n", five + ((A % 5) / 3));
			}
		}
	}
	return 0;
}
