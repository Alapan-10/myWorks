#include<stdio.h>
void main() {
	int x = 10;
	int *y = &x;
	printf("The value held by x: (%%d, x) =  %d\n", x);
	printf("The address of location named x: (%%p, &x) = %p\n", &x);
	printf("The address held by pointer y: (%%p, y) = %p\n", y);
	printf("The value that is pointed to by the pointer y: (%%d, *y) = %d\n", *y);
	printf("The address that holds the address of x: (%%p, &y) = %p\n", &y);
}
