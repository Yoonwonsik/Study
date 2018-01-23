#include <stdio.h>

int main()
{
	char str[50],str1[50],str2[50];

	printf("문구를 입력하세요 :");
	gets(str);
	printf("%s\n", str);
	printf("문구를 입력하세요 :");
	gets(str1);
	printf("%s\n", str1);
	printf("문구를 입력하세요 :");
	gets(str2);
	printf("%s\n", str2);

	return 0;
}