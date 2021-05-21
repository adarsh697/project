def add(*args):
    res=0
    for num in args:
        res+=num
        print(num);
    return res

print("result"+add(10,20,30,40))
