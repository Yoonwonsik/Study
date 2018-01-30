#include <stdio.h>
#include <string.h>

int main()
{
	char word[100]; // 100만큼 문자 공간 생성
	printf("문자를 입력하세요 : ");
	scanf("%s", &word); // 문자 입력 받기
	char printword;
	for (int i = 0; i <= strlen(word); i = i + 1)
	{
		printword = word[i];
		printf("%c",printword);
		if ((i+1)%10 == 0)
		{
			printf("\n");
		}
	}
	
	return 0;
}