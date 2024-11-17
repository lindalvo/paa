//
// Created by 60659211220 on 17/11/2024.
//
#include <stdio.h>
#include <stdlib.h>

void Primo(int n)
{
  int j = 2;
  while ((j < n) && ((n % j) != 0) ) {
     j++;
  }
  if (j == n) {
    printf("%d e primo", n);
  }
  else{
    printf("%d nao e primo", n);
  }
   
}

int main() {
  Primo(7);
  return 0;
}