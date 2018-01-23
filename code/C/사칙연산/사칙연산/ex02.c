#include <stdio.h>

int sum(int a, int b);
int min(int a, int b);
int mul(int a, int b);
int div(int a, int b);
int rem(int a, int b);

int main()
{
	int A, B;
	printf("A B 입력하세요 :");
	scanf("%d %d", &A, &B);
	printf("A : %d\nB : %d\n", A, B);
	printf("A + B : %-2d\n", sum(A, B));
	printf("A - B : %-2d\n", min(A, B));
	printf("A * B : %-2d\n", mul(A, B));
	printf("A / B : %-2d\n", div(A, B));
	printf("A %% B : %-2d\n", rem(A, B));

	return 0;
}
int sum(int a, int b)
{
	int sum = a + b;
	return sum;
}
int min(int a, int b)
{
	int min = a - b;
	return min;
}
int mul(int a, int b)
{
	int mul = a * b;
	return mul;
}
int div(int a, int b)
{
	int div = a / b;
	return div;
}
int rem(int a, int b)
{
	int rem = a % b;
	return rem;
}