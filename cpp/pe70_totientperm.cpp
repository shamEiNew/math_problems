#include "pe69_totient.h"
#include <iostream>
using namespace std;

int n_over_phi_n(int n){
    float  min = 2;
    int val = 2;
    for (int k=2; k <= n;k++){
        float phi_k = phi(k);
        float k_over_phi_k = k/phi_k;
        if (k_over_phi_k <= min) {
            min = k_over_phi_k;
            val = k;
        }
    }
    return val;
}

int main(){
    int n_min = n_over_phi_n(10);
    cout << n_min;
    return 0;
}

