#include <stdio.h>
#include <string.h>

int main()
{
	char word[100]; // 100��ŭ ���� ���� ����
	printf("���ڸ� �Է��ϼ��� : ");
	scanf("%s", &word); // ���� �Է� �ޱ�
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