#include<stdio.h>
void main() {
	char *name[] = {"lionel messi", "cristiano ronaldo", "robert lewandowski", "zlatan ibrahimovic"};
	printf("The God: %s\n", *(name+3)+7);
}
