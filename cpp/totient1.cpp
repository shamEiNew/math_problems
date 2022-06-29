// O(sqrt(n)) implementation of totient function
#include<iostream>
using namespace std;

int phi(int n) {
    //Intialize phi(n)
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        //Check whether i divides n
        if (n % i == 0) {
            //Check whether i divides the remaining quotient
            while (n % i == 0)
                n /= i;
            //Subtract all multiples of i from n
            result -= result / i;
        }
    }
    // In case n has no divisors
    if (n > 1)
        result -= result / n;
    return result;
}

int main() {
    int count = phi(100);
    cout << count;
    return 0;
}
