import numpy as np


def checkm(min_l, diff):
    max_num =  max(min_l)
    max_index =  min_l.index(max_num)
    while sum(min_l) != 10**6:
        if diff >= 0:
            diff = max_num - diff
            min_l[max_index]=0
        elif diff < 0:
            max_num =  max(min_l)
            max_index =  min_l.index(max_num)
            min_l[max_index]=max_num + diff
        elif sum(min_l) == 10**6:
            break
    return min_l
    

def is_dpossible(m):
    result = []
    m_shape = m.shape[0]
    for i in range(m_shape):
        min = np.amin(m[i], axis=0)
        s = sum(min)
        if s >= 10**6:
            if s==10**6:
                result.append(min)
            elif s-10**6 > 0:
                diff = s-10**6
                min_l = list(min)
                result1 = checkm(min_l, diff)
                result.append(result1)
        else:
            result.append("IMPOSSIBLE")
    return result


if __name__=="__main__":
    n = int(input().strip())
    rc = []
    for _ in range(n):
        temp = []
        for _ in range(3):
            temp.append(
                list(map(int, input().strip().split())))
        rc.append(temp)
    rc =  np.array(rc)
    result =  is_dpossible(rc)
    for x in range(rc.shape[0]):
        if len(result[x])==4:
         print(f"Case #{x+1}: {result[x][0]} {result[x][1]} {result[x][2]} {result[x][3]}")
        else:
            print(f"Case #{x+1}: {result[x]}")