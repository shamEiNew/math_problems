import numpy as np
import sys
import os
import matplotlib.pyplot as plt

def fibonacci_vec(n):
    F_0 = np.array([[1],[1]])
    A = np.array([[1, 1],[1, 0]])

    for i in range(n):
        A = np.matmul(A, A)

    return np.matmul(A, F_0)


def fibonacci_sequence(n):
    """
    For small n <= 1000
    """
    fib_sequence = np.array([1, 1], dtype='int64')
    def fib_term(i, fib_sequence):
        """
        Note that i>=2
        """
        return np.append(fib_sequence, fib_sequence[i-1]+fib_sequence[i-2])

    
    if n < 2:
        return fib_sequence
    else:
        for i in range(2, n):
            fib_sequence = fib_term(i, fib_sequence)

    return fib_sequence

if __name__=="__main__":
    plt.rc('grid', linestyle="-", color='black')
    x_val =fibonacci_sequence(80)
    print(x_val)
    y_val = np.array([len(str(i)) for i in x_val])
    fig , ax = plt.subplots(figsize=(12, 8))
    ax.plot(range(len(x_val)), y_val,c='green')
    ax.plot(range(len(x_val)), y_val, 'o--',c='grey', alpha=0.3)
    ax.set_xlabel("n (index of number in sequence)")
    ax.set_ylabel("number of digits in nth term of sequence")
    fig.suptitle("Number of digits in Fibonaacci sequence")
    plt.grid(axis='both', color='0.95')
    plt.show()
    fig.savefig("./Week2/static/fibterms")