#include <stdio.h>

int main()
{
	char s1[101];
	int length = 0;
	printf("������ ���� : ");
	scanf("%d",&length);
	printf("���� : ");
	scanf("%s", &s1);
	int sum=0;
	for (int i = 0; i < length; i = i + 1)
	{
		sum = sum + s1[i] - '0';
	}
	printf("%d\n", sum);

	return 0;
}