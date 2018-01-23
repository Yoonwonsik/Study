#include <stdio.h>

int main()
{
	int N = 0;
	printf("정수입력 : ");
	scanf("%d", &N);
	for (int j=1; j<=N; j=j+1) //행
	{
		for (int i = 1; i <= j; i = i + 1) //열
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}