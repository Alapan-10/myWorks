#include<stdio.h>
void main() {
	int a[10];
	for( int i=0; i<10; i++) {
		*(a+i) = i*i;
		printf("%d\t", a[i]);
		printf("%p\n", a+i);
	}
}
