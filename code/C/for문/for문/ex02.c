#include <stdio.h>

int main()
{
	int N = 0;
	printf("�����Է� : ");
	scanf("%d", &N);
	for (int i = 0; i < N; i = i + 1)
	{
		printf("%d\n", N-i);
	}
	return 0;
}