#include <stdio.h>
#include <stdlib.h>
// Fibonacci sequence
// 1, 1, 2, 3, 5, 8

int fib(int n){
    if(n == 0 || n == 1)
        return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(void){
    printf("%d", fib(4));
    return 0;
}