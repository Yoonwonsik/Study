#include <stdio.h>
#include <stdlib.h>
int fuction1065(int a)
{
	int count = 0;
	int b=0; //1000 자리수
	int c=0; // 100 자리수
	int d=0; //  10 자리수
	int e=0; //   1 자리수

	if (a < 100)
	{
		for (int i = 0; i < a; i++)
		{
			count++;
		}
	}
	if (a > 100)
	{
		count = 99;
		for (int i = 100; i < a; i++)
		{
			// 각 자리수 구하기
			c = (i / 100) - 10 * b;
			d = (i / 10) - 100 * b - 10 * c;
			e = i - 1000 * b - 100 * c - 10 * d;
			if ((c-d)==(d-e)) count++;
		}
	}
	if (a > 1000)
	{
		for (int i = 1000; i < a; i++)
		{
			// 각 자리수 구하기
			b = i / 1000;
			c = (i / 100) - 10 * b;
			d = (i / 10) - 100 * b - 10 * c;
			e = i - 1000 * b - 100 * c - 10 * d;
			if ((b-c)==(c - d) == (d - e)) count++;
		}
	}
	printf("%d", count);

	return 0;
}



int main()
{
	int a;
	scanf("%d", &a);
	fuction1065(a);
}