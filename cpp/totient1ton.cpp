#include <iostream>
#include <vector>
// O(sqrt(n log log n)) implementation of totient function  
using namespace std;
void phi_1_to_n(int n) {
    vector<int> phi(n + 1);
    //Initialzing all Phi(i)
    for (int i = 0; i <= n; i++)
        phi[i] = i;

    for (int i = 2; i <= n; i++) {
        if (phi[i] == i) {
            //removing multiples of i
            for (int j = i; j <= n; j += i)
                phi[j] -= phi[j] / i;
        }
    }
    for (int i: phi)
        cout << i << " ";
}

int main(){
    phi_1_to_n(100);
    return 0;
}
