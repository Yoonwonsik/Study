#include <stdio.h>

int main()
{
	int a, b = 0;
	int c, d = 0;
	printf("두수 a,b를 입력하세요 :");
	scanf("%d %d", &a, &b);
	printf("두수의 합은 : %d\n",a+b);

	printf("두수 c,d를 입력하세요 :");
	scanf("%d %d", &c, &d);
	printf("두수의 차는 : %d\n", c - d);

	system("pause");

	return 0;
}