#include <stdio.h>

int main()
{
	char str[50],str1[50],str2[50];
	printf("������ �Է��ϼ��� :");
	scanf("%s", &str);
	printf("%s\n", str);
	printf("������ �Է��ϼ��� :");
	scanf("%s", &str1);
	printf("%s\n", str1);
	printf("������ �Է��ϼ��� :");
	gets(str2);
	printf("%s\n", str2);

	return 0;
}