#include <stdio.h>
#include <stdlib.h>


void sort(int str[],int a)
{
	for (int i = 0; i < a - 1; i = i + 1)
	{
		for (int j = 1; j < a; j = j + 1)
		{
			if (str[i] < str[j])
			{
				int temp;
				temp = str[i];
				str[i] = str[j];
				str[j] = temp;
			}
		}
	}
}

void main()
{
	int N, Y;
	int score[100] = { 0, };
	scanf("%d", &N);
	for (int i = 0; i < N; i = i + 1)
	{
		scanf("%d", &Y);
		score[i] = Y;
	}
	sort(score,N);
	int max = score[0];
	int sum = 0;
	for (int j = 0; j < N; j = j + 1)
	{
		score[j] = (double)score[j] / max *100;
		sum = sum + score[j];
	}
	double result = (double)(sum) / N;
	printf("%.2lf", result);
}
