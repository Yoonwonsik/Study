#include <stdio.h>
#include <stdlib.h>

void main()
{
	int num = 0, count = 0, a = 0, b = 0, c = 0, k;
	scanf("%d", &num);
	k = num;
	for (;;)
	{
		a = k / 10;
		b = k % 10;
		c = (a + b) % 10;
		printf("%d %d %d ", a, b, c);
		a = b;
		b = c;
		k = a * 10 + b;
		count = count + 1;
		printf("%d\n",k);
		if (num == k) break;
	}
	printf("%d", count);
}