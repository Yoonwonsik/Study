#include <stdio.h>
#include <stdlib.h>

int main()
{
	int tc, n, str[100] = { 0, };

	scanf("%d", &tc);

	for (int i = 0; i < tc; i = i + 1)
	{
		int sum=0, cnt = 0;
		double avg = 0.0;

		scanf("%d", &n);

		for (int j = 0; j < n; j = j + 1)
		{
			scanf("%d", &str[j]);
			sum = sum + str[j];
		}
		avg = (double)sum / (double)n;

		for (int k = 0; k < n; k = k + 1)
		{
			if (str[k] > avg)
				cnt = cnt + 1;
		}

		avg = (double)cnt / n;

		printf("%.3lf%%\n", avg * 100);
	}
}
