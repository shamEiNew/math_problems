# Coded By: Armaan Nougai

#Brute Force

# Project Euler 18 and 67





with open('./static/bigmaxpathsum.txt','r') as FILE:

    Data = FILE.readlines()

    arr = [list(map(int,(j.split()))) for j in Data]

    result_arr = arr[0]

    for row in arr[1:]:

        new_result_arr = []

        for x,value in enumerate(row):

            if x==0:

                # 1st element of row

                new_result_arr += [value+result_arr[0]]

            elif x==len(row)-1:

                # last element of row

                new_result_arr += [value + result_arr[-1]]

            else:

                # mid-elements of row

                new_result_arr += [value+max(result_arr[x],result_arr[x-1])]

        result_arr = new_result_arr



    print(max(result_arr))

