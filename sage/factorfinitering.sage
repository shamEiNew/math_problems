def base_ring():
    size = 7
    base_ring.<x> = PolynomialRing(GF(size))
    p_x =((x+4)^8)*(x^2+4)*(x^3+3)^2
    return base_ring, p_x

def factor_ring(base_ring,p_x):
    ideal_p_x = base_ring.ideal([p_x])
    factor_ring = base_ring.quotient_ring(ideal_p_x)
    if p_x.is_irreducible():
        return p_x.degree()
    else:  
        factors = p_x.factor()
        factors = list(factors)

    return factor_ring, factors

def prod_length(base_ring, factors):
    p = base_ring.characteristic()
    m_val = [poly[1] for poly in factors]
    p_degree = [poly[0].degree() for poly in factors]
    s_val=[]
    k_val=[]
    for m in m_val:
        h=1
        while p^h<m:
            h=h+1
        s_val.append(h)
        
    for j,m in zip(s_val, m_val):
        k_tuple=[0]*(j+2)
        for i in range(0, j+2):
            h=0
            while h*(p**i)<m:
                h=h+1
            k_tuple[i]=h-1
        k_val.append(k_tuple)
    k_i = []
    for i,j in enumerate(s_val):
        temp=[]
        temp.append(p**(p_degree[i])-1)
        for t in range(1, j+1):
            temp.append(p_degree[i]*(k_val[i][t-1]-2*k_val[i][t]+k_val[i][t+1]))
        k_i.append(temp)
    
    return p,m_val,s_val, k_val,k_i

size =7
F, p=base_ring()
Q, factors = factor_ring(F, p)
print(prod_length(F,factors))