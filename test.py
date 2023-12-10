test1 = [1,2,4,5,6,7,8,9,10]

test2 = [12,5,9,10]

res = [a+b for a,b in zip(test1, test2)] 

print(sum(res))