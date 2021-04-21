import random as rd
buy=int(input("몇장 구매하시겠습니까? "))
lotto={}
lotto_num=list(range(1,46))
for i in range(1,buy+1):
    for y in range(0,6):
        lotto["%d 회차"%i]=rd.sample(lotto_num,k=6)
print(lotto)