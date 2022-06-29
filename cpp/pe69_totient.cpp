#include <iostream>
using namespace std;

int phi(int n) {
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}

int n_over_phi_n(){
    float  max = 2;
    int val = 2;
    for (int k=2; k <= 1000000;k++){
        float phi_k = phi(k);
        float k_over_phi_k = k/phi_k;
        if (k_over_phi_k >= max) {
            max = k_over_phi_k;
            val = k;
        }
    }
    return val;
}