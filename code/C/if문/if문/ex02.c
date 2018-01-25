#include <stdio.h>


int main()
{
	/*int a = 0, b = 0, c = 0;
	printf("세 정수 입력:");
	scanf("%d %d %d", &a,&b,&c);

	if (a > b)
	{
		if (b > c)
		{
			printf("%d\n", b);
		}
		else
		{
			if (a > c)
			{
				printf("%d\n", c);
			}
			else
			{
				printf("%d\n", a);
			}
		}
	}
	else
	{
		if (b > c)
		{
			if (a > c)
			{
				printf("%d\n", a);
			}
			else
			{
				printf("%d\n", c);
			}
		}
		else
		{
			printf("%d\n", b);
		}
	}*/

	int arr[3], i, j, tmp;

	scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

	for (i = 0; i<3; i++)

		for (j = 0; j<2; j++)

			if (arr[j] >= arr[j + 1]) {

				tmp = arr[j];

				arr[j] = arr[j + 1];

				arr[j + 1] = tmp;

			}

	printf("%d\n", arr[1]);

	return 0;
}