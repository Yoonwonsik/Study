#include <stdio.h>

int main()
{
	int N = 0;
	printf("정수입력 : ");
	scanf("%d",&N);
	for (int i = 1; i <= N; i = i + 1)
	{
		printf("%d\n", i);
	}
	return 0;
}