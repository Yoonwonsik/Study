#include <stdio.h>




int main()
{
	for (;;)
	{
		int A; // ����Ű�μ�
		printf("���� Ű�μ��� �Է��ϼ��� :");
		scanf("%d", &A);
		int five = A / 5; // 5�� ������
		if (A < 0)
			break;
		if (A > 0)
		{
			for (; five >= 0;)
			{
				if ((A % 5) % 3 != 0)
				{

				}
				five = five - 1;
			}
			printf("5Ű�� : %d\n", five);
			printf("3Ű�� : %d\n", ((A % 5) / 3));
			printf("�հ� : %d\n", five + ((A % 5) / 3));
		}
	}
	return 0;
}
