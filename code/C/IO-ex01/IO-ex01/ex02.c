#include <stdio.h>

int main()
{
	int a, b = 0;
	int c, d = 0;
	printf("�μ� a,b�� �Է��ϼ��� :");
	scanf("%d %d", &a, &b);
	printf("�μ��� ���� : %d\n",a+b);

	printf("�μ� c,d�� �Է��ϼ��� :");
	scanf("%d %d", &c, &d);
	printf("�μ��� ���� : %d\n", c - d);

	system("pause");

	return 0;
}