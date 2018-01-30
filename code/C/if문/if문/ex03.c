#include <stdio.h>
#include <stdlib.h>


void main()
{
	int N, X, Y;
	int str[10000];
	scanf("%d %d", &N, &X);
	for (int i = 0; i < N; i = i + 1)
	{
		scanf("%d", &Y);
		str[i] = Y;
	}
	for (int i = 0; i < N; i = i + 1)
	{
		if (X > str[i]) printf("%d ", str[i]);
	}
}
