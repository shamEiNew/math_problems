#include<iostream>
using namespace std;

int mystery(int n)
{
   
    int x=2, count=0;
    while (x < n) {
        x*=2;
        count++;
        }
    cout << "I just got executed!\n";
    return count;
}

int main(){
int c = mystery(16);
cout<< c;
return 0;
}