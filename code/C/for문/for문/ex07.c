#include <stdio.h>

int main()
{
	int N = 0;
	printf("�����Է� : ");
	scanf("%d", &N);
	for (int j = 1; j <= N; j = j + 1) //��
	{
		for (int i = 1; i <= j-1; i = i + 1) //�������
		{
			printf(" ");
		}
		for (int i = N; i >= j; i = i - 1) //�����
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}