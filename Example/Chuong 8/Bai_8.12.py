x = int(input("Nhập số x: "))
flag = True 
if x < 2 :
    print(x, "Không phải số nguyên tố")
else:
    for i in range(2, x):
        if x%i == 0:
            flag = False
            break
    if flag:
        print(x, " là số nguyên tố")
    else:
        print(x, " không phải là số nguyên tố")


x = int(input("Nhập số x: "))
if (x % 1 ==0 and x % x ==0):
    print("a")
else:
    print("B")            