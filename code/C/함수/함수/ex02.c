#include <stdio.h>
#include <stdlib.h>
int fuction1065(int a)
{
	int count = 0;
	int b=0; //1000 �ڸ���
	int c=0; // 100 �ڸ���
	int d=0; //  10 �ڸ���
	int e=0; //   1 �ڸ���

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
			// �� �ڸ��� ���ϱ�
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
			// �� �ڸ��� ���ϱ�
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