#include <stdio.h>

int main(void) {
   int a, b;
   int sum, sub, mul, inv, div, rest;

   printf("a와 b의 값을 입력하세요 :");
   scanf("%d %d", &a, &b);
   sum = a + b;
   sub = a - b;
   mul = a * b;
   inv = -a;
   div = a / b;
   rest = a % b;
   printf("a의 값은 : %d, b의 값은 : %d\n덧셈 : %d\n뺄셈 : %d\n곱셈 : %d\na의 음수 연산 : %d\n 몫은 %d 나머지는 %d", a, b, sum, sub, mul, inv, div, rest);

   return 0;
}