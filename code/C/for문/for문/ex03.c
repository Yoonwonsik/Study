#include <stdio.h>

int main()
{
	int N = 0;
	printf("�ܼ��Է� : ");
	scanf("%d", &N);
	for (int i = 1; i <= 9; i = i + 1)
	{
		printf("%d * %d = %2d\n", N,i,N*i);
	}
	return 0;
}