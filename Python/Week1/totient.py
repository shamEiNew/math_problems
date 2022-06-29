  
import matplotlib.pyplot as plt
import numpy as np
# plt.rcParams['text.usetex'] = True

def phi_1_to_n(n:int) -> list:
    phi = []
    for i in range(0, n+1):
        phi.append(i)

    for i in range(2, n+1):
        if (phi[i] == i):
            for j in range(i, n+1,i):
                phi[j] -= phi[j] // i
    return phi[1:]

if __name__=="__main__":
    n = 10000
    phi_n=phi_1_to_n(n)
    fig, ax=plt.subplots()
    ax.scatter(range(0, n), phi_n,s=1.5, marker='.')
    ax.plot(np.arange(0, n), np.arange(0, n)-1,'r--', c='r')
    ax.set_ylabel("φ(n)")
    ax.set_xlabel("n")
    ax.set_title("Totient function (φ(n)) values for n≤10000")
    plt.savefig("totient10000")
    plt.show()


