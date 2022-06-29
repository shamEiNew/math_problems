#include<iostream>
using namespace std;

int main(){

//Incrementing in cpp
int a[] = {1, 2, 3, 4, 5};
int i = 2; // Second index number of the array a[]
a[i]++;
printf("%d %d\n", i, a[i]);
a[i++];
printf("%d %d\n", i, a[i]);
return 0;
}
